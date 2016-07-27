from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoWeb.views.home', name='home'),
    # url(r'^DjangoWeb/', include('DjangoWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #rl(r'^admin/', include(admin.site.urls)),
    #url(r'^main.html$','Web.views.main',name='main.html'),
    url(r'',include('Web.urls')),
)
