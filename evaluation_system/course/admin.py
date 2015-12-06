from django.contrib import admin
from ..course.models import Course, Course_User
# Register your models here.


admin.site.register(Course_User)
admin.site.register(Course)
