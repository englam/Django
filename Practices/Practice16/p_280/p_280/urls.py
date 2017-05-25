from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

import views
import restaurants.views


urlpatterns = patterns('',

    url(r'^here/', views.here),
    url(r'^here2/', views.here2.as_view()),


    url(r'^index/', views.index),
    url(r'^index2/', views.index2.as_view())

                       ,
    url(r'^list_restaurants/', views.list_restaurants),
    url(r'^list_restaurants2/', views.list_restaurants2.as_view()), #for views required login or not
    #url(r'^list_restaurants2/', login_required(views.list_restaurants2.as_view())), #for urls.py required


    url(r'^menu3/', views.menu3),
    url(r'^menu/(?P<pk>\d+)/$', views.menu3View.as_view()),
    #url(r'^menu/(?P<id>\d+)/$', views.menu3View.as_view()),

    url(r'^comment/(\d{1,5})/$', views.comment),
    url(r'^comment2/(?P<pk>\d+)/$', views.comment2.as_view()),

)
