from django.shortcuts import render
from ..questions.models import Question
from django.views.generic import TemplateView
from django.contrib.auth import logout, authenticate

from django.shortcuts import redirect
from .models import User


def user_logout(request):
    logout(request)
    return redirect("/")

def home(request):
	if not request.user.is_authenticated():
		return redirect("/login")
	if request.user.type == 'student':
		return redirect('/evaluate')
	body = "Welcome please register or login"
	title = "Evaluation System"
	user = request.user
	print user.type
	questions = Question.objects.all()
	body = "Hello %s" %user
	context = {
		"title": title,
		"body": body,
		"user": user,
		"que": questions,
	}
	return render(request, "home.html", context)