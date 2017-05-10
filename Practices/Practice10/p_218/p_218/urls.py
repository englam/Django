from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import index
from django.contrib.auth.views import login, logout



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_218.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^index/', index),
    url(r'^accounts/login/', login),
    url(r'^accounts/logout/', logout),
    url(r'^accounts/profile/', index),
)
