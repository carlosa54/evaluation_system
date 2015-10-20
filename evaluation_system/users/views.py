from django.shortcuts import render
from questions.models import Question
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required
def home(request):
	body = "Welcome please register or login"
	title = "Evaluation System"
	user = request.user
	questions = Question.objects.all()
	if request.user.is_authenticated():
		body = "Hello %s" %user
	context = {
		"title": title,
		"body": body,
		"user": user,
		"que": questions,
	}
	return render(request, "home.html", context)