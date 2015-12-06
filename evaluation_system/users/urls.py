from django.conf.urls import url

from . import views

urlpatterns = [
	url(
		r'^$', 
		views.home, 
		name='home'
	),
    url(
        r'^logout$',
        views.user_logout,
        name="logout"
    ),
    url(r'^addstudent/$', 
		views.AddStudentView.as_view() , 
		name='addstudent'
	),
]