from django.conf.urls import patterns, include, url

from restaurants.views import menu, menu2,meta, list_restaurants, menu3, menu4, comment, comment2, get_c,set_c,use_session, session_test
from views import welcome

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'p_160.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^menu/', menu),
    url(r'^menu2/', menu2),
    url(r'^meta/', meta),
    url(r'^welcome/', welcome),
    url(r'^restaurants_list/', list_restaurants),
    url(r'^menu3/', menu3),
    url(r'^menu4/(\d{1,5})/$', menu4),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^comment2/(\d{1,5})/$', comment2),
    url(r'^get_c/', get_c),
    url(r'^set_c/', set_c),
    url(r'^use_session/', use_session),
    url(r'^session_test/', session_test),

)
