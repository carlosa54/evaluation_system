from django.db import models
from djangoyearlessdate.models import YearField
from ..questions.models import Question
from ..course.models import Course
from ..users.models import User
import datetime

# Create your models here.
class Evaluation(models.Model):
	academic_year = YearField(default = datetime.date.today().strftime("%Y"))
	course = models.ForeignKey(Course)
	semester = models.IntegerField()
	seccion = models.CharField(max_length= 3)
	questions = models.ManyToManyField(Question, through = "Evaluation_Question")

	def __unicode__(self):
		return self.course.name

	def group_names(self):
		return ', '.join([a.name for a in self.groups.all()])
	group_names.short_description = "Group names"


class Evaluation_Question(models.Model):
	evaluation = models.ForeignKey(Evaluation)
	question = models.ForeignKey(Question)

class Group(models.Model):
	name = models.CharField(max_length=200)
	students = models.ManyToManyField(User, limit_choices_to= {'type':'student'}, through = "Group_User")
	evaluation = models.ForeignKey(Evaluation, related_name = 'groups') 


	#Method added for displaying all students of the group in the admin page ManyToMany 
	def student_names(self):
		return ', '.join([a.first_name for a in self.students.all()])
	student_names.short_description = "Student names"

class Group_User(models.Model):
	group = models.ForeignKey(Group)
	student = models.ForeignKey(User, limit_choices_to= {'type':'student'})

	def __unicode__(self):
		return self.group.name

	

