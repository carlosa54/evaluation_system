from django.db import models
from users.models import User, Group
from questions.models import Question
# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=200)
	section = models.CharField(max_length=3)
	questions = models.ManyToManyField(Question)
	groups = models.ManyToManyField(Group)
	proffesor = models.ForeignKey(User, limit_choices_to= {'type':'proffesor'})
