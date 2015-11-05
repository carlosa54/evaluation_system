from django.db import models
from ..users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Answer(models.Model):
	score = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)], null=True)
	answered_by = models.ForeignKey(User, limit_choices_to= {'type':'student'}, related_name = 'answered_by', null = True, blank = True)
	answered_for = models.ForeignKey(User, limit_choices_to= {'type':'student'}, related_name = 'answered_for', null = True, blank = True)

class Question(models.Model):
	question_text = models.TextField()
	answers = models.ForeignKey(Answer, null= True, blank = True)

	def __unicode__(self):
		return self.question_text