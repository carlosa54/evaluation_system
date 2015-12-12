from django.shortcuts import render
from ..questions.models import Question
from django.views.generic import TemplateView
from django.contrib.auth import logout, authenticate
from .forms import UserCreationForm
from django import forms
from django.shortcuts import redirect
from .models import User
from ..course.models import Course
from ..evaluation.models import Group_User, Group


def user_logout(request):
    logout(request)
    return redirect("/")

def home(request):
	if not request.user.is_authenticated():
		return redirect("/login")
	if request.user.type == 'professor':
		return redirect('/dashboard')
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

class AddStudentView(TemplateView):
	template_name = "dashboard/addstudent.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		form = UserCreationForm(request.POST)
		form.fields['type'].widget = forms.HiddenInput()

		if form.is_valid():
			new_user = form.save()

			grp = Group.objects.get(pk = request.POST['group'])

			link = Group_User(student = new_user, group = grp)
			link.save()
			context["form"] = form
			context["success"] = "Student created"
		else:
			context["form"] = form
			context["error"] = "Student failed"
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		groups = Group.objects.filter(evaluation = request.session['eva_id']).order_by('name')
		context["groups"] =  groups

		print groups
		form = UserCreationForm()
		form.fields['type'].widget = forms.HiddenInput()

		context['form'] = form
		return self.render_to_response(context)

