from django.contrib import admin
from ..questions.models import Question, Answer
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	fields = ('question_text',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)