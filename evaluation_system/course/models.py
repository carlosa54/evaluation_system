from django.db import models
from ..users.models import User
from ..questions.models import Question
#from ..evaluation.models import Evaluation
# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=200)
	students = models.ManyToManyField(User, limit_choices_to= {'type':'student'})
	#evaluation = models.ForeignKey(Evaluation, related_name = 'groups') 

	def __unicode__(self):
		return self.name

	#Method added for displaying all students of the group in the admin page ManyToMany 
	def student_names(self):
		return ', '.join([a.first_name for a in self.students.all()])
	student_names.short_description = "Student names"

class Course(models.Model):
	name = models.CharField(max_length=200)
	proffesor = models.ManyToManyField(User, limit_choices_to= {'type':'proffesor'}, related_name = 'proffesor', through= "Course_User")

	def group_names(self):
		return ', '.join([a.name for a in self.groups.all()])
	group_names.short_description = "Group names"

class Course_User(models.Model):
	course = models.ForeignKey(Course)
	proffesor = models.ForeignKey(User)
