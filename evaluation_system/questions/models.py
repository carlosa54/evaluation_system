from django.db import models
from users.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Question(models.Model):
	question_text = models.TextField()
	score = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(10)], null=True)
	answered_by = models.ForeignKey(User, limit_choices_to = {'type':'student'}, null=True)
