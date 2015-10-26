from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ProfessorEvaluateForm
from ..course.models import Course
from .models import Group_User

# Create your views here.
class ProfessorEvaluateView(TemplateView):
	template_name = "evaluation/evaluate.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		form = ProfessorEvaluateForm()

		context['form'] = form

		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)

class StudentEvaluateView(TemplateView):
	template_name = "evaluation/studentevaluate.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")			
		context = self.get_context_data(**kwargs)

		form = ProfessorEvaluateForm()

		context['form'] = form

		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)


class StudentChoicesView(TemplateView):
	template_name = "evaluation/studentchoices.html"

	def get(self,request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)

		context = self.get_course_and_groups(request.user, context)

		return self.render_to_response(context)

	def get_course_and_groups(self, user, context):
		group = Group_User.objects.filter(student = user)
		context['groups'] = group
		return context






