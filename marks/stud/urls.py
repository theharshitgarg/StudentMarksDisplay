from django.conf.urls import patterns, include, url

from django.contrib import admin
from stud import views
 
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'marks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', views.index, name='index'),
	url(r'^line/$', views.line, name='line'),
	url(r'^result/$', views.display, name='result'),
	url(r'^phy/$', views.displayPhysics, name='physics'),
	url(r'^chem/$', views.displayChemistry, name='chemistry'),
	url(r'^math/$', views.displayMathematics, name='mathematics'),
	url(r'^total/$', views.total, name='total'),
	url(r'^(?P<stud_id>\d+)/hd/$', views.hd, name='hd'),
)



