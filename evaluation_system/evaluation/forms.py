from django import forms
from .models import Evaluation, Evaluation_Question, Group

class ProfessorEvaluateForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['academic_year', 'course', 'semester', 'seccion']

class AddGroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name', 'evaluation']