from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import AddQuestionForm
from ..evaluation.models import Evaluation, Evaluation_Question

# Create your views here.
class AddQuestionView(TemplateView):
	template_name = "dashboard/addquestion.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		form = AddQuestionForm(request.POST)

		if form.is_valid():
			new_question = form.save()

			evaluation_que = Evaluation_Question(evaluation = form.cleaned_data['evaluation'], question= new_question)
			evaluation_que.save()

			context["form"] = form
			context["success"] = "Question created"
		else:
			context["form"] = form
			context["error"] = "Question failed"
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		form = AddQuestionForm()
		
		form.fields['evaluation'].queryset = Evaluation.objects.filter(course__professor= request.user)

		context['form'] = form
		return self.render_to_response(context)