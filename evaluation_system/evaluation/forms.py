from django import forms
from .models import Evaluation

class ProfessorEvaluateForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['academic_year', 'course', 'semester', 'seccion', 'questions']