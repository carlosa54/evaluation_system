from django.shortcuts import redirect
from django.views.generic import TemplateView
from ..course.models import Course
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


		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)

class SetCourseDashboardView(TemplateView):

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")		
		context = self.get_context_data(**kwargs)

		if 'course_id' in kwargs:
			request.session['course_id'] = kwargs['course_id']
		if 'eva_id' in kwargs:
			request.session['eva_id'] = kwargs['eva_id']

		return redirect("/evaluate")





		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)