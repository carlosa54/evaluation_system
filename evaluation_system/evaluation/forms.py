from django import forms
from .models import Evaluation, Evaluation_Question

class ProfessorEvaluateForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['academic_year', 'course', 'semester', 'seccion']