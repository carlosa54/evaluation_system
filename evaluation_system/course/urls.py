from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^addcourse/$', 
		views.AddCourseView.as_view(), 
		name='addcourse'
	),	
]