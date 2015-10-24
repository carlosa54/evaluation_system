from django import forms
from .models import Evaluation

class EvaluateForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['academic_year', 'course', 'semester', 'seccion', 'questions']