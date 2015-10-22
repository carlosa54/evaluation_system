from django.db import models
from ..users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Answer(models.Model):
	score = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)], null=True)
	answered_by = models.CharField(max_length = 200)
	answered_for = models.CharField(max_length = 200)

class Question(models.Model):
	question_text = models.TextField()
	answers = models.ForeignKey(Answer)