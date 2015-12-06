from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^addquestion/$', 
		views.AddQuestionView.as_view() , 
		name='addquestion'
	),

]