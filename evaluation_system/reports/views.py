from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from ..evaluation.models import Evaluation, Group_User



class showProfessorReport(TemplateView):
	template_name= "report/professorReport.html"

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		context["evaluations"] = Evaluation.objects.filter(course__professor = request.user, created_by = request.user.id)


		return self.render_to_response(context)

class showStudentReport(TemplateView):
	template_name= "report/studentReport.html"

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "student":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		group = Group_User.objects.filter(student = request.user)

		context["group"] = group

		if not group:
			context['error'] = "You're not assigned to any courses"


		return self.render_to_response(context)
