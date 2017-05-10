from django.conf.urls import patterns, include, url
from django.contrib import admin

'''Method two'''
from views import login, index, logout



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_210.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),

    url(r'^accounts/login/', login),
    url(r'^accounts/logout/', logout),
    url(r'^index/', index),


)
