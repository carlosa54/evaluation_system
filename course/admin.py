from django.contrib import admin
from course.models import Course
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields' : ['name', 'groups', 'proffesor']}),
	]


admin.site.register(Course, CourseAdmin)