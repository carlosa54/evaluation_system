from django import forms
from .models import Evaluation, Evaluation_Question, Group

class ProfessorEvaluateForm(forms.ModelForm):
	class Meta:
		model = Evaluation
		fields = ['name','academic_year', 'course', 'semester', 'seccion']

class AddGroupForm(forms.ModelForm):
	class Meta:
		model = Group
		fields = ['name', 'evaluation']

class AddAnswerForm(forms.Form):
	def __init__(self, *args, **kwargs):
		extra = kwargs.pop('extra')
		#personas = kwargs.pop('persons')
		super(AddAnswerForm, self).__init__(*args, **kwargs)
		CHOICES=[('1','1'), ('2','2'),('3','3'),('4','4'),('5','5')]

		#person = forms.ChoiceField(choices = personas)
		for i, question in enumerate(extra):
			self.fields['question_%s' % question.id] = forms.ChoiceField(choices = CHOICES,label = question, widget = forms.RadioSelect())


	def extra_answers(self):
		for name, value in self.cleaned_data.items():
			if name.startswith('question_'):
				yield (self.fields[name].label, value)