from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import menu, menu2

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_menu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^menu/', menu),
    url(r'^menu2/', menu2),
)
