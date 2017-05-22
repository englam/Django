from django.conf.urls import patterns, include, url
from django.contrib import admin
from restaurants.views import menu, menu2, menu3

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_258.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^menu/', menu),
    url(r'^menu2/', menu2),
    url(r'^menu3/', menu3),
)
