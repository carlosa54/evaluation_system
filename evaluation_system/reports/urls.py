from django.conf.urls import url

from . import views

urlpatterns = [
	url(
        r'^report$',
        views.showProfessorReport.as_view(), 
		name='report'
    ),
	url(
        r'^studentreport$',
        views.showStudentReport.as_view(), 
		name='studentreport'
    ),
]