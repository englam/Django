from django.conf.urls import patterns, include, url

from views import index, register, login
from django.contrib import admin
from restaurants.views import list_restaurants

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_228.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', register),
    url(r'^accounts/login/', login),
    url(r'^index/', index),
    url(r'^restaurants_list/', list_restaurants),
)
