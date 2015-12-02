from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from ..course.models import Course



class showProfessorReport(TemplateView):
	template_name= "report/professorReport.html"

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		context["curso"] = Course.objects.filter(professor = request.user)


		return self.render_to_response(context)
