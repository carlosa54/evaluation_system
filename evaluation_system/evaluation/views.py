from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ProfessorEvaluateForm, AddGroupForm, AddAnswerForm
from ..course.models import Course
from .models import Group_User, Group, Evaluation
from ..users.models import User
from ..questions.models import Question, Answer
from django import template

# Create your views here.
class ProfessorEvaluateView(TemplateView):
	template_name = "dashboard/evaluate.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		form = ProfessorEvaluateForm(request.POST)
		form.fields['course'].queryset = Course.objects.filter(professor = request.user)
		if form.is_valid():
			new_evaluation = form.save(commit=False)
			new_evaluation.created_by = request.user.id
			form.save()

			context["form"] = form
			context["success"] = "Evaluation created"
		else:
			
			context["form"] = form
			context["error"] = "Evaluation failed"
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)
		

		form = ProfessorEvaluateForm()

		form.fields['course'].queryset = Course.objects.filter(professor = request.user)

		context['form'] = form

		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)


class StudentChoicesView(TemplateView):
	template_name = "evaluation/studentchoices.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)

		for name, value in request.POST.items():
			if name.startswith('question_'):
				prop = name.split('_')
				que = Question.objects.get(pk = prop[1])
				eva = Evaluation.objects.get(pk = request.POST['evaluation'])
				ans = Answer(evaluation_id = eva.id ,question = que, score = value, student = request.user.id, student_evaluated = request.POST['student'])
				ans.save()
				stud = Group_User.objects.get(student = request.POST['student'], group__evaluation = eva.id)
				stud.save()
		
		return redirect("/choices")

	def get(self,request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		
		context = self.get_course_and_groups(request.user, context)

		return self.render_to_response(context)


	def get_course_and_groups(self, user, context):
		groups = Group.objects.filter(students = user)
		
		context['groups'] = groups
		return context

class AddGroupView(TemplateView):
	template_name = "dashboard/addgroup.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		form = AddGroupForm(request.POST)
		form.fields['evaluation'].queryset = Evaluation.objects.filter(course= request.session['course_id'])

		if form.is_valid():
			new_group = form.save()

			context["form"] = form
			context["success"] = "Group created"
		else:
			context["form"] = form
			context["error"] = "Group failed"

		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		form = AddGroupForm()
		#To show only evaluations that are in the professor courses
		form.fields['evaluation'].queryset = Evaluation.objects.filter(course= request.session['course_id'])

		context['form'] = form
		return self.render_to_response(context)