from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import test, test1, test2, test5, test7,test9, test10, test11

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_246.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', test),
    url(r'^test1/', test1),
    url(r'^test2/', test2),
    url(r'^test5/', test5),
    url(r'^test7/', test7),
    url(r'^test9/', test9),
    url(r'^test10/', test10),
    url(r'^test11/', test11),
)
