from django.conf.urls import url

from . import views

urlpatterns = [
	url(
        r'^dashboard$',
        views.DashboardView.as_view(), 
		name='dashboard'
    ),
	url(
        r'^dashboard/(?P<course_id>[0-9]+)$',
        views.SetCourseDashboardView.as_view(), 
		name='coursedash'
    ),
]