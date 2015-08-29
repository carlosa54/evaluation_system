from django.db import models
from users.models import User

# Create your models here.

class Question(models.Model):
	question_text = models.TextField()
	CHOICES = [(i,i) for i in range(11)]
	score = models.IntegerField(CHOICES)
	answered_by = models.ForeignKey(User)
