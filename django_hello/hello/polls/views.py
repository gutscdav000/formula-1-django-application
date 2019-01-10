# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#django imports
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.apps import apps
from django.http import HttpResponseRedirect, Http404

# project imports
#from django.db import models
from models import *
from forms import TableForm

#python imports
import math, json

PAGE_LEN = 1000.00


#def test_base(request):
#    return render(request, 'base.html', {"tables" : "lol",})

# Create your views here.
def index(request):

    # if request.method == 'POST':
    #     form = TableForm(request.POST)
    #     if form.is_valid():
    #         return render(request, 'index.html', {"form" : form})
    # else:x
    #     form = TableForm()
    #     return render(request, 'index.html', {"form" : form})
    raw_tables = raw_query()
    # decode raw queryset objects
    tables = [rawQSet[0].decode('utf-8') for rawQSet in raw_tables]
    table_recs = [
            Drivers.objects.count(),
            Constructors.objects.count(),
            Circuits.objects.count(),
            Status.objects.count(),
            Seasons.objects.count(),
            Races.objects.count(),
            Qualifying.objects.count(),
            Results.objects.count(),
            DriverStandings.objects.count(),
            ConstructorStandings.objects.count(),
            ConstructorResults.objects.count(),
            LapTimes.objects.count(),
            PitStops.objects.count(),
    ]

    return render(request, 'index.html', {"tables" : tables, "table_recs" : table_recs, })



def circuits(request, page_num = 1):
    circuit_lst = Circuits.objects.all()
    return render(request, 'circuits.html', {"circuit_lst": circuit_lst, "page_num" : page_num, "rec_cnt" : circuit_lst.count()})

def constructor_results(request, page_num = 1):
    page_num = int(page_num)
    const_res_lst = ConstructorResults.objects.all()
    records = const_res_lst.count()
    pages = math.ceil(records / PAGE_LEN)

    # debugging info
    print "rec count: ", records
    print "pg cnt: ", pages
    print "pg num", page_num

    # page range logic (grab ~1000 records)
    if page_num <= 1:
        gte = 1
        lte = PAGE_LEN
    else:
        gte = (page_num - 1) * PAGE_LEN + 1
        lte = page_num * PAGE_LEN

    query_filt = const_res_lst.filter(constructorresultsid__gte = gte, constructorresultsid__lte = lte)


    return render(request, 'constructor_results.html', {"const_res_lst" : query_filt, "page_num" : page_num, "rec_cnt" : query_filt.count()})


def constructor_standings(request, page_num = 1):
    page_num = int(page_num)
    const_stnd_lst = ConstructorStandings.objects.all()
    records = const_stnd_lst.count()
    pages = math.ceil(records / PAGE_LEN)

    # debugging info
    print "rec count: ", records
    print "pg cnt: ", pages
    print "pg num", page_num

    # page range logic (grab ~1000 records)
    if page_num <= 1:
        gte = 1
        lte = PAGE_LEN
    else:
        gte = (page_num - 1) * PAGE_LEN + 1
        lte = page_num * PAGE_LEN

    query_filt = const_stnd_lst.filter(constructorstandingsid__gte = gte, constructorstandingsid__lte = lte)


    return render(request, 'constructor_standings.html', {"const_stnd_lst" : query_filt, "page_num" : page_num, "rec_cnt" : query_filt.count()})


def constructors(request, page_num = 1):
    constructors = Constructors.objects.all()
    return render(request, 'constructors.html', {"constructors" : constructors, "page_num" : page_num, "rec_cnt" : constructors.count()})

def driver_standings(request, page_num = 1):
    page_num = int(page_num)
    driver_stdngs = DriverStandings.objects.all()
    records = driver_stdngs.count()
    pages = math.ceil(records / PAGE_LEN)

    # debugging info
    print "rec count: ", records
    print "pg cnt: ", pages
    print "pg num", page_num

    # page range logic (grab ~1000 records)
    if page_num <= 1:
        gte = 1
        lte = PAGE_LEN
    else:
        gte = (page_num - 1) * PAGE_LEN + 1
        lte = page_num * PAGE_LEN

    query_filt = driver_stdngs.filter(driverstandingsid__gte = gte, driverstandingsid__lte = lte)


    return render(request, 'driver_standings.html', {"driver_stdngs" : query_filt, "page_num" : page_num, "rec_cnt" : query_filt.count()})


def drivers(request, page_num = 1):
    drivers = Drivers.objects.all()
    return render(request, 'drivers.html', {"drivers" : drivers, "page_num" : page_num, "rec_cnt" : drivers.count()})

# ******* Bug with model *************
def lap_times(request, page_num = 1):
    page_num = int(page_num)
    laps = LapTimes.objects.all()
    records = laps.count()
    pages = math.ceil(records / PAGE_LEN)

    # debugging info
    print "rec count: ", records
    print "pg cnt: ", pages
    print "pg num", page_num

    # page range logic (grab ~1000 records)
    if page_num <= 1:
        gte = 1
        lte = PAGE_LEN
    else:
        gte = (page_num - 1) * PAGE_LEN + 1
        lte = page_num * PAGE_LEN

    query_filt = laps.filter(id__gte = gte, id__lte = lte)


    return render(request, 'lap_times.html', {"laps" : query_filt, "page_num" : page_num, "rec_cnt" : query_filt.count()})

# ******* Bug with model *************
def pit_stops(request, page_num = 1):
    page_num = int(page_num)
    pit_stops = PitStops.objects.all()
    records = pit_stops.count()
    pages = math.ceil(records / PAGE_LEN)

    # debugging info
    print "rec count: ", records
    print "pg cnt: ", pages
    print "pg num", page_num

    # page range logic (grab ~1000 records)
    if page_num <= 1:
        gte = 1
        lte = PAGE_LEN
    else:
        gte = (page_num - 1) * PAGE_LEN + 1
        lte = page_num * PAGE_LEN

    query_filt = pit_stops.filter(id__gte = gte, id__lte = lte)


    return render(request, 'pit_stops.html', {"pit_stops" : query_filt, "page_num" : page_num, "rec_cnt" : query_filt.count()})


def qualifying(request, page_num = 1):
    page_num = int(page_num)
    quals = Qualifying.objects.all()
    records = quals.count()
    pages = int(math.ceil(records / PAGE_LEN))

    # debugging info
    print "rec count: ", records
    print "pg cnt: ", pages
    print "pg num", page_num

    # page range logic (grab ~1000 records)
    if page_num <= 1:
        gte = 1
        lte = PAGE_LEN
    else:
        gte = (page_num - 1) * PAGE_LEN + 1
        lte = page_num * PAGE_LEN

    query_filt = quals.filter(qualifyid__gte = gte, qualifyid__lte = lte)

    return render(request, 'qualifying.html', {"quals" : query_filt, "page_num" : page_num, "rec_cnt" : query_filt.count()})

def races(request, page_num = 1):
    races = Races.objects.all()
    return render(request, 'races.html', {'races' : races, "page_num" : page_num, "rec_cnt" : races.count()})

def results(request, page_num = 1):
        page_num = int(page_num)
        res = Results.objects.all()
        records = res.count()
        pages = int(math.ceil(records / PAGE_LEN))

        # debugging info
        print "rec count: ", records
        print "pg cnt: ", pages
        print "pg num", page_num

        # page range logic (grab ~1000 records)
        if page_num <= 1:
            gte = 1
            lte = PAGE_LEN
        else:
            gte = (page_num - 1) * PAGE_LEN + 1
            lte = page_num * PAGE_LEN

        query_filt = res.filter(resultid__gte = gte, resultid__lte = lte)

        return render(request, 'results.html', {"res" : query_filt, "page_num" : page_num, "rec_cnt" : query_filt.count()})

def status(request, page_num = 1):
    stat = Status.objects.all()
    return render(request, 'status.html', {'stat' : stat, "page_num" : page_num, "rec_cnt" : stat.count()})

def seasons(request, page_num = 1):
    seasons = Seasons.objects.all()
    return render(request, 'seasons.html', {'seasons' : seasons, "page_num" : page_num, "rec_cnt" : seasons.count()})

def handle_form(request):
    try:
        choice = request.POST['choice']
        choice = int(choice)
    except Exception as e:
        return HttpResponse(e)
    else:

        responsePaths = {
            1 : '/polls/circuits/',
            2 : '/polls/constructor_results/',
            3 : '/polls/constructor_standings/',
            4 : '/polls/constructors/',
            5 : '/polls/driver_standings/',
            6 : '/polls/drivers/',
            7 : '/polls/lap_times/',
            8 : '/polls/pit_stops/',
            9 : '/polls/qualifying/',
           10 : '/polls/races/',
           11 : '/polls/results/',
           12 : '/polls/status/',
           13 : '/polls/seasons/'

        }

        response = responsePaths.get(choice, "invalid")
        if response != "invalid":
            return HttpResponseRedirect(response)
        else:
            raise Http404()

def update_form(request):
    path = request.POST['request_path']
    headList = request.POST['headList'].split(',')


    #put form arguments in a list
    queryDict = dict(request.POST.iterlists())
    keyLst = sorted([(key, queryDict.get(key)[0]) for key in queryDict.keys() if key.isdigit()])

    dbUpDict = {}
    for i in range(len(keyLst)):
        print ("***pair: ", headList[i], keyLst[i][1])
        dbUpDict[headList[i]] = keyLst[i][1]

    Circuits.objects.filter(circuitid = int(keyLst[0][1])).update(**dbUpDict)


    if path != None:
        return HttpResponseRedirect(path)
    else:
        raise Http500()

def get_table_headers(request):
    table_headers = ['circuitid', 'circuitref', 'name', 'location', 'country', 'lat', 'lng', 'alt', 'url']
    response_data = {}

    response_data['result'] = 'Success'
    response_data['message'] = table_headers

    return HttpResponse(json.dumps(response_data), content_type = 'polls/json')
