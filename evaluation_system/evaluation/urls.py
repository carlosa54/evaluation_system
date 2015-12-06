from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^evaluate/$', 
		views.ProfessorEvaluateView.as_view(), 
		name='evaluate'
	),
	url(r'^choices/$', 
		views.StudentChoicesView.as_view() , 
		name='studentchoices'
	),
	url(r'^addgroup/$', 
		views.AddGroupView.as_view() , 
		name='addgroup'
	),
]