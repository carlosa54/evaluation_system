from django.contrib import admin
from .models import Evaluation, Evaluation_Question, Group, Group_User
# Register your models here.
admin.site.register(Evaluation)
admin.site.register(Evaluation_Question)
admin.site.register(Group)
admin.site.register(Group_User)