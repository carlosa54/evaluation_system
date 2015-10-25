from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import ProfessorEvaluateForm

# Create your views here.
class ProfessorEvaluateView(TemplateView):
	template_name = "dashboard/evaluate.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)

		form = ProfessorEvaluateForm(request.POST)

		if form.is_valid():
			new_evaluation = form.save()

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

