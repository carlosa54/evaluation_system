from django.contrib import admin
from questions.models import Question
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'score', 'answered_by')
	fields = ('question_text',)

admin.site.register(Question, QuestionAdmin)