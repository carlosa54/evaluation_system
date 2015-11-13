from django.db import models
from ..users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Question(models.Model):
	question_text = models.TextField()

	def __unicode__(self):
		return self.question_text

class Answer(models.Model):
	score = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)], null=True)
	question = models.ForeignKey(Question, null = True)
	evaluation_id = models.IntegerField(null=True)
	student = models.IntegerField(null=True)
	student_evaluated = models.IntegerField(null=True)

	class Meta:
		unique_together = ("question", "evaluation_id", "student", "student_evaluated")