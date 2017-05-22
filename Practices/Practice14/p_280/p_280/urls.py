from django.conf.urls import patterns, include, url

import views


urlpatterns = patterns('',

    url(r'^here/', views.here),
    url(r'^here2/', views.here2.as_view()),
    url(r'^index/', views.index),
    url(r'^index2/', views.index2.as_view()),

)
