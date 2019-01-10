# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

import sys
# my code
sys.path.insert(0, '/Projects/django_hello/db/')
from restore_db import connect_to_db, close_db_connection


def raw_query():
    conn = connect_to_db("localhost", "f1_db", "postgres", "postgres")
    cursor = conn.cursor()
    cursor.execute("""
    select tablename from pg_catalog.pg_tables
    where schemaname = 'public'
    and tablename not like '%django%'
    and tablename not like '%auth%';
    """)
    row = cursor.fetchall()
    close_db_connection(conn)
    return row

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Circuits(models.Model):
    circuitid = models.AutoField(primary_key=True)
    circuitref = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    alt = models.IntegerField(blank=True, null=True)
    url = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'circuits'


class ConstructorResults(models.Model):
    constructorresultsid = models.AutoField(primary_key=True)
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceid', blank=True, null=True)
    constructorid = models.ForeignKey('Constructors', models.DO_NOTHING, db_column='constructorid', blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'constructor_results'


class ConstructorStandings(models.Model):
    constructorstandingsid = models.AutoField(primary_key=True)
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceid', blank=True, null=True)
    constructorid = models.ForeignKey('Constructors', models.DO_NOTHING, db_column='constructorid', blank=True, null=True)
    points = models.FloatField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(max_length=255, blank=True, null=True)
    wins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'constructor_standings'


class Constructors(models.Model):
    constructorid = models.AutoField(primary_key=True)
    constructorref = models.CharField(max_length=255)
    name = models.CharField(unique=True, max_length=255)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'constructors'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DriverStandings(models.Model):
    driverstandingsid = models.AutoField(primary_key=True)
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceid', blank=True, null=True)
    driverid = models.ForeignKey('Drivers', models.DO_NOTHING, db_column='driverid', blank=True, null=True)
    points = models.FloatField()
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(max_length=255, blank=True, null=True)
    wins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'driver_standings'


class Drivers(models.Model):
    driverid = models.AutoField(primary_key=True)
    driverref = models.CharField(max_length=255)
    number = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    forename = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    dob = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'drivers'


class LapTimes(models.Model):
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceid', blank=True, null=True)
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driverid', blank=True, null=True)
    lap = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    milliseconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lap_times'


class PitStops(models.Model):
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceid', blank=True, null=True)
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driverid', blank=True, null=True)
    stop = models.IntegerField()
    lap = models.IntegerField()
    time = models.TimeField()
    duration = models.CharField(max_length=255, blank=True, null=True)
    milliseconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pit_stops'


class Qualifying(models.Model):
    qualifyid = models.AutoField(primary_key=True)
    raceid = models.ForeignKey('Races', models.DO_NOTHING, db_column='raceid', blank=True, null=True)
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driverid', blank=True, null=True)
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING, db_column='constructorid', blank=True, null=True)
    number = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    q1 = models.CharField(max_length=255, blank=True, null=True)
    q2 = models.CharField(max_length=255, blank=True, null=True)
    q3 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qualifying'


class Races(models.Model):
    raceid = models.AutoField(primary_key=True)
    year = models.IntegerField()
    round = models.IntegerField()
    circuitid = models.ForeignKey(Circuits, models.DO_NOTHING, db_column='circuitid', blank=True, null=True)
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    url = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'races'


class Results(models.Model):
    resultid = models.AutoField(primary_key=True)
    raceid = models.ForeignKey(Races, models.DO_NOTHING, db_column='raceid', blank=True, null=True)
    driverid = models.ForeignKey(Drivers, models.DO_NOTHING, db_column='driverid', blank=True, null=True)
    constructorid = models.ForeignKey(Constructors, models.DO_NOTHING, db_column='constructorid', blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    grid = models.IntegerField()
    position = models.IntegerField(blank=True, null=True)
    positiontext = models.CharField(max_length=255, blank=True, null=True)
    positionorder = models.IntegerField()
    points = models.FloatField()
    laps = models.IntegerField()
    time = models.CharField(max_length=255, blank=True, null=True)
    milliseconds = models.IntegerField(blank=True, null=True)
    fastestlap = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    fastestlaptime = models.CharField(max_length=255, blank=True, null=True)
    fastestlapspeed = models.CharField(max_length=255, blank=True, null=True)
    statusid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'


class Seasons(models.Model):
    year = models.IntegerField(primary_key=True)
    url = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasons'


class Status(models.Model):
    statusid = models.AutoField(primary_key=True)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'status'
