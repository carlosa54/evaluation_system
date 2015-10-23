from django.conf.urls import url

from . import views

urlpatterns = [
	url(
		r'^evaluate/$', 
		views.EvaluateView.as_view(), 
		name='evaluate'
	),
]