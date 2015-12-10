from django.shortcuts import redirect
from django.views.generic import TemplateView
from ..course.models import Course
from ..evaluation.models import Evaluation
# Create your views here.
class DashboardView(TemplateView):
	template_name = "dashboard/courses.html"

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")		
		context = self.get_context_data(**kwargs)

		courses = Course.objects.filter(professor= request.user)
		context['courses'] = courses

		if 'course_id' in request.session:
			del request.session['course_id']
			del request.session['course_name']
		if 'eva_id' in request.session:
			del request.session['eva_id']
			del request.session['eva_name']


		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)

class SetCourseDashboardView(TemplateView):

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")		
		context = self.get_context_data(**kwargs)
		if 'eva_id' in request.session:
			del request.session['eva_id']
			del request.session['eva_name']
		if 'course_id' in kwargs:
			request.session['course_id'] = kwargs['course_id']
			request.session['course_name'] = Course.objects.get(pk= kwargs['course_id']).name
		if 'eva_id' in kwargs:
			request.session['eva_id'] = kwargs['eva_id']
			request.session['eva_name'] = Evaluation.objects.get(pk= kwargs['eva_id']).name
		return redirect("/evaluate")





		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)