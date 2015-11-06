from django import forms
from .models import Question
from ..evaluation.models import Evaluation
class AddQuestionForm(forms.ModelForm):
	eva = Evaluation.objects.all()
	evaluation = forms.ModelChoiceField( queryset = eva)
	class Meta:
		model = Question
		fields = ['question_text']