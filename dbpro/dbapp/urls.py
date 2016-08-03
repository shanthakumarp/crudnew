from django.conf.urls import patterns,url

#from dbapp import views

urlpatterns = patterns('',
	url(r'^show/', 'dbapp.views.show', name = 'show'),
	url(r'^insert/', 'dbapp.views.insert',name = 'insert'),
	url(r'^delete/(?P<person_id>\d+)/', 'dbapp.views.delete', name = 'delete'),
	url(r'^edit/(?P<person_id>\d+)/', 'dbapp.views.edit', name = 'edit'),
	url(r'^update_favor/','dbapp.views.edit_favorites', name= 'edit_favorites'),
	)