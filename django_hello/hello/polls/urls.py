from django.conf.urls import url
from polls import views

#urlpatterns = patterns('',
#                        url(r'^$', views.index, name = 'index'),
#)
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^find-data/$', views.handle_form, ),
    url(r'^circuits/$', views.circuits, name = 'circuits'),
    url(r'^constructor_results/$', views.constructor_results, name = 'constructor results'),
    url(r'^constructor_results/(?:page=(?P<page_num>\d+))?$', views.constructor_results, name = 'constructor results'),
    url(r'^constructor_standings/$', views.constructor_standings, name = 'constructor standings'),
    url(r'^constructor_standings/(?:page=(?P<page_num>\d+))?$', views.constructor_standings, name = 'constructor standings'),
    url(r'^constructors/$', views.constructors, name = 'constructors'),
    url(r'^driver_standings/$', views.driver_standings, name = 'driver_standings'),
    url(r'^driver_standings/(?:page=(?P<page_num>\d+))?$', views.driver_standings, name = 'driver standings'),
    url(r'^drivers/$', views.drivers, name = 'drivers'),
    url(r'^lap_times/$', views.lap_times, name = 'lap_times'),
    url(r'^lap_times/(?:page=(?P<page_num>\d+))?$', views.lap_times, name = 'lap_times'),
    url(r'^pit_stops/$', views.pit_stops, name = 'pit_stops'),
    url(r'^pit_stops/(?:page=(?P<page_num>\d+))?$', views.pit_stops, name = 'pit_stops'),
    url(r'^qualifying/$', views.qualifying, name = 'qualifying'),
    url(r'^qualifying/(?:page=(?P<page_num>\d+))?$', views.qualifying, name = 'qualifying'),
    url(r'^races/$', views.races, name = 'races'),
    url(r'^results/$', views.results, name = 'results'),
    url(r'^results/(?:page=(?P<page_num>\d+))?$', views.results, name = 'results'),
    url(r'^status/$', views.status, name = 'status'),
    url(r'^seasons/$', views.seasons, name = 'seasons'),
    url(r'^update_form/$', views.update_form, name = 'update_form'),
    url(r'^get_table_headers/$', views.get_table_headers, name = 'get_table_headers'),

    # testing js lib
    url(r'^test_d3js/$', views.test_d3js, name = 'test_d3js'),
    url(r'^brush_zoom/$', views.brush_zoom, name = 'brush_zoom'),
    url(r'^partial_area_under_curve/$', views.partial_area_under_curve, name = 'partial_area_under_curve'),

]
