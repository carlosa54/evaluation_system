from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import redirect

# Create your views here.
class EvaluateView(TemplateView):
	template_name = "evaluation/evaluate.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)

		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)