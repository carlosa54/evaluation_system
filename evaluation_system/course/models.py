from django.db import models
from ..users.models import User
from ..questions.models import Question
#from ..evaluation.models import Evaluation
# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=200)
	professor = models.ManyToManyField(User, limit_choices_to= {'type':'professor'}, related_name = 'professor', through= "Course_User")

	def __unicode__(self):
		return self.name
		
class Course_User(models.Model):
	course = models.ForeignKey(Course)
	professor = models.ForeignKey(User)
