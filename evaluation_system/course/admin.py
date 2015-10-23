from django.contrib import admin
from ..course.models import Course, Group
# Register your models here.


class CourseAdmin(admin.ModelAdmin):
	list_display = ('name', 'group_names', 'proffesor')
	

class GroupAdmin(admin.ModelAdmin):
	list_display = ('name', 'student_names')

admin.site.register(Course, CourseAdmin)
admin.site.register(Group, GroupAdmin)