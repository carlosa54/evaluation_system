from django.db import models
from users.models import User
from questions.models import Question
# Create your models here.

class Group(models.Model):
	name = models.CharField(max_length=200)
	students = models.ManyToManyField(User, limit_choices_to= {'type':'student'})

	#Method added for displaying all students of the group in the admin page ManyToMany 
	def student_names(self):
		return ', '.join([a.first_name for a in self.students.all()])
	student_names.short_description = "Student names"

class Course(models.Model):
	name = models.CharField(max_length=200)
	section = models.CharField(max_length=3)
	questions = models.ManyToManyField(Question)
	groups = models.ManyToManyField(Group)
	students = models.ManyToManyField(User, limit_choices_to = {'type': 'student'}, related_name = 'student')
	proffesor = models.ForeignKey(User, limit_choices_to= {'type':'proffesor'})