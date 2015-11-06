from django.views.generic import TemplateView
from django.shortcuts import redirect
from .forms import CourseForm
from models import Course_User

# Create your views here.
class AddCourseView(TemplateView):
	template_name = 'dashboard/addcourse.html'

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")
		context = self.get_context_data(**kwargs)
		form = CourseForm(request.POST)

		if form.is_valid():
			new_course = form.save()

			professor_course = Course_User(course = new_course, professor = request.user)
			professor_course.save()

			context["form"] = form
			context["success"] = "Course created"
		else:
			context["form"] = form
			context["error"] = "Course failed"
		return self.render_to_response(context)

	def get(self, request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect("/login")	
		if not request.user.type == "professor":
			return redirect("/")		
		context = self.get_context_data(**kwargs)

		form = CourseForm()

		context['form'] = form

		#context = self.retrieve_persons(request.user, context)
		return self.render_to_response(context)