from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ProfessorEvaluateForm
from ..course.models import Course
from .models import Group_User
from ..users.models import User
from django import template

# Create your views here.
class ProfessorEvaluateView(TemplateView):
	template_name = "dashboard/evaluate.html"

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

	register = template.Library()

	def get(self,request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)

		context = self.get_course_and_groups(request.user, context)

		return self.render_to_response(context)

	def get_course_and_groups(self, user, context):
		group = Group_User.objects.filter(student = user)

		variable = []

		for students in group:
			test = Group_User.objects.filter(group = students)
			print test
			for student in test:
				variable.append(student)
			 
			# for student in test:
			# 	if not student.group.id in variable:
			# 		variable[student.group.id] = [student.student]
			# 	else:
			# 		variable[student.group.id].append(student.student)
			# 	print student.student.first_name + ' ' + student.group.name
		print variable

		context['groups'] = group
		context['students'] = variable
		return context

	@register.filter
	def get_at_index(list, index):
		return list[index]
		
	def firstchoice(request):
    		if request.method == 'POST':
        		try:
            			choice = request.POST['group-name']
            			# TODO use flag
        		except KeyError:
            			print 'No group !'
			return render_to_response('studentevaluate.html', {},
        		context_instance=RequestContext(request))






