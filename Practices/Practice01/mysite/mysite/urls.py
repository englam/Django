from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import here, add, math, math2, math3, math4, math5

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^here1/$',here), #path , object
    url(r'^(\d{1,2})/plus/(\d{1,2})/$',add), 
    url(r'^(\d{1,2})/math/(\d{1,2})/$',math), 
    url(r'^(\d{1,2})/math2/(\d{1,2})/$',math2),
    url(r'^(\d{1,2})/math3/(\d{1,2})/$',math3),
    url(r'^(\d{1,2})/math4/(\d{1,2})/$',math4),
    url(r'^(\d{1,2})/math5/(\d{1,2})/$',math5),

)
