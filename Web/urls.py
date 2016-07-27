from django.conf.urls import patterns,include,url

urlpatterns = patterns('Web.views',
    url(r'^$','main',name='main.html'),
    url(r'^main.html/','main',name='mian.html'),
    url(r'^index.html/','index',name='index.html'),
    url(r'^addonu.html/','addonu',name='addonu.html'),
    url(r'^ceshi.html/','ceshi',name='ceshi.html'),
    url(r'^wgnlcs.html/','wgnlcs',name='wgnlcs.html'),
    url(r'^test.html/','test',name='test.html'),
    url(r'^addonudatas/?','SendOnu'),
    url(r'^addonucmd/?','AddOnuCmd'),
    url(r'^addonurun/?','Addonurun'),
)
