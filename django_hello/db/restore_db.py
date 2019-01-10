import os, csv
import psycopg2 as psy

table_types = {


    "circuits" : [
             "number",
            "varchar",
            "varchar",
            "varchar",
            "varchar",
            "number",
            "number",
            "number",
            "varchar",
    ],

    "constructor_results" : [
            "number",
            "number",
            "number",
            "number",
            "varchar",
    ],

    "constructors" : [
            "number",
            "varchar",
            "varchar",
            "varchar",
            "varchar",
    ],

    "constructor_standings" : [
            "number",
            "number",
            "number",
            "number",
            "number",
            "varchar",
            "number",
    ],

    "drivers" : [

            "number",
            "varchar",
            "number",
            "varchar",
            "varchar",
            "varchar",
            "date",
            "varchar",
            "varchar",
    ],

    "driver_standings" : [
            "number",
            "number",
            "number",
            "number",
            "number",
            "varchar",
            "number",
    ],

    "lap_times" : [
            "number",
            "number",
            "number",
            "number",
            "number",
            "varchar",
            "number",
    ],

    "pit_stops" : [
            "number",
            "number",
            "number",
            "number",
            "number",
            "time",
            "varchar",
            "number",
    ],

    "qualifying" : [
            "number",
            "number",
            "number",
            "number",
            "number",
            "number",
            "varchar",
            "varchar",
            "varchar",
    ],

    "races" : [
        "number",
        "number",
        "number",
        "number",
        "varchar",
        "date",
        "time",
        "varchar",
    ],

    "results" : [
        "number",
        "number",
        "number",
        "number",
        "number",
        "number",
        "number",
        "varchar",
        "number",
        "number",
        "number",
        "varchar",
        "number",
        "number",
        "number",
        "varchar",
        "varchar",
        "number",
    ],

    "seasons" : [
        "number",
        "varchar"
    ],

    "status" : [
        "number",
        "varchar",
    ]

}

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]



def read_table(fileName, conn, error_count, dupe_count):

    prefix = 'backup_data/f1db_csv/'

    with open(os.path.join(prefix,fileName)) as csv_file:
        #csv_reader = csv.reader(csv_file)
        csv_reader = unicode_csv_reader(csv_file)

        # print("*************rows******************")
        # for row in csv_reader:
        #     print(row)
        # print("*************rows******************")

        id = 1
        tmp = 0
        for row in csv_reader:

            try:
                # REGULAR TABLES
                #tmp = insert_db_data(conn, fileName, row)
                #dupe_count += tmp

                # FOREIGN KEY TABLES
                id, tmp = insert_db_data_foreign_keys(conn, fileName, row, id)
                id += 1
                dupe_count += tmp

            except Exception as e:
                error_count += 1
                id -= 1
                f = open('error_log.txt', 'a+')
                string = "file: " + fileName + "\n" + "error: " + str(e)
                f.write(string)
                string = "record: " + str(row)
                f.write(string)
                f.write('\n\n')
                f.close()
                pass
    return error_count, dupe_count


def connect_to_db(host, dbname, user, password):
    try:
        conn = psy.connect(host=host, database=dbname, user=user, password=password)

    except exception as e:
        print e

    else:
        print "*** connection suceeded ***"

        return conn

def close_db_connection(conn):
    try:
        conn.close()
    except exception as e:
        print e

    else:
        if conn.closed == 1:
            print "*** connection closed ***"
        else:
            print "*** connection couldn't be closed ***"

def insert_db_data(conn, tableName, valList):
    dupe_count = 0

    table = tableName
    if tableName[-4:] == '.csv':
        table = tableName.split('.')[0]
    table = 'public.' + table
    if table == 'public.driver':
        table = 'public.drivers'

    print table

    with conn.cursor() as curs:
        sql = "INSERT INTO " + table + " VALUES ("
        sql = str(sql)
        print valList
        for i in range(len(valList) - 1):
            sql = sql + "'" + data_type_as_string(valList[i], table_types[table.split('.')[1]][i]) + "', "
        #last elem has no comma
        sql = sql + "'" + data_type_as_string(valList[len(valList) - 1], table_types[table.split('.')[1]][len(valList) - 1]) + "');"

        print "QUERY: "
        print sql
        try:
            curs.execute(sql)
        except psy.IntegrityError:
            dupe_count += 1
            print "*** duplicate record ***"
            curs.execute('ROLLBACK;')
        else:
            conn.commit()

        return dupe_count


##############################################################################
# foreign key table insert function
def insert_db_data_foreign_keys(conn, tableName, valList, id):
    dupe_count = 0

    table = tableName
    if tableName[-4:] == '.csv':
        table = tableName.split('.')[0]
    table = 'public.' + table

    print table

    with conn.cursor() as curs:
        sql = "INSERT INTO " + table + " VALUES (" + str(id) + ", "
        sql = str(sql)

        #sql = "INSERT (raceid, driverid, lap, position, time, milliseconds) INTO VALUES ("
        #sql = str(sql)

        for i in range(len(valList) - 1):
            sql = sql + "'" + data_type_as_string(valList[i], table_types[table.split('.')[1]][i]) + "', "
        #last elem has no comma
        sql = sql + "'" + data_type_as_string(valList[len(valList) - 1], table_types[table.split('.')[1]][len(valList) - 1]) + "');"

        print "QUERY: "
        print sql
        try:
            curs.execute(sql)
        except psy.IntegrityError:
            print "*** duplicate record ***"
            curs.execute('ROLLBACK;')
            id -= 1
        else:
            conn.commit()

    return id, dupe_count
##############################################################################



def data_type_as_string(rawVar, db_type):
    #print "rawVar, db_type:\t" + str(rawVar) + ", " + db_type

    #if rawVar == '\N' or '\\N':
    #if rawVar == r'\\N' or rawVar == r'\N':
    if rawVar == u'\\\\N' or rawVar == u'\\N':
        if db_type == "number":
            #print "null cond"
            return '999999999'
        elif db_type == "varchar":
            return ""
        elif db_type == "date":
            return "2001-01-01"
        elif db_type == "time":
            return "00:00:00"

    if db_type == "number":
        #print "not null cond"
        return rawVar
    elif db_type == "varchar":
        if "\\" in rawVar:
            indx = rawVar.find("\\")
            out = rawVar[:indx] + '\\' + rawVar[indx:]
            return out
        if "'" in rawVar:
            indx = rawVar.find("'")
            out = rawVar[:indx] + "\'" + rawVar[indx:]
            return out

        return rawVar
    elif db_type == "date":
        return rawVar
    elif db_type == "time":
        return rawVar
    else:
        print "there was a data type error"
        return "there was a data type error"


def update_nulls(conn, table, col, colVal):
    sql = "update public."+ table + " set " + col +" = NULL where " + col +" = " + colVal
    try:
        with conn.cursor() as curs:
            curs.execute(sql)
    except Exception as e:
        print e
    else:
        conn.commit()



#MAIN

# - results

# error_count = 0
# dupe_count = 0
# conn = connect_to_db("localhost", "f1_db", "postgres", "postgres")
#
#
# #for tble in [ 'circuits', 'constructors', 'driver', 'seasons', 'status', 'races', 'qualifying', 'driver_standings', 'constructor_standings', 'constructor_results', 'results']:
# for tble in ['pit_stops', 'lap_times',]:
#     file = tble + '.csv'
#     error_count, dupe_count = read_table(file, conn, error_count, dupe_count)
#
#
# close_db_connection(conn)
# print "errors, dupes: ", error_count, dupe_count
