from django.db import models
from ..users.models import User
from ..questions.models import Question
#from ..evaluation.models import Evaluation
# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=200)
	proffesor = models.ManyToManyField(User, limit_choices_to= {'type':'proffesor'}, related_name = 'proffesor', through= "Course_User")

	def group_names(self):
		return ', '.join([a.name for a in self.groups.all()])
	group_names.short_description = "Group names"

class Course_User(models.Model):
	course = models.ForeignKey(Course)
	proffesor = models.ForeignKey(User)
