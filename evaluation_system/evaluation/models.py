from django.db import models
from djangoyearlessdate.models import YearField
from ..questions.models import Question
from ..course.models import Course
from ..users.models import User
import datetime

# Create your models here.
class Evaluation(models.Model):
	name = models.CharField(max_length= 200, default = 'Unknown')
	academic_year = YearField(default = datetime.date.today().strftime("%Y"))
	course = models.ForeignKey(Course)
	semester = models.IntegerField()
	seccion = models.CharField(max_length= 3)
	questions = models.ManyToManyField(Question, through = "Evaluation_Question")
	created_by = models.IntegerField(null=True)

	def __unicode__(self):
		return self.name

	def group_names(self):
		return ', '.join([a.name for a in self.groups.all()])
	group_names.short_description = "Group names"


class Evaluation_Question(models.Model):
	evaluation = models.ForeignKey(Evaluation)
	question = models.ForeignKey(Question)

	def __unicode__(self):
		return self.question.question_text

class Group(models.Model):
	name = models.CharField(max_length=200)
	students = models.ManyToManyField(User, limit_choices_to= {'type':'student'}, through = "Group_User", related_name = 'group')
	evaluation = models.ForeignKey(Evaluation, related_name = 'groups') 


	#Method added for displaying all students of the group in the admin page ManyToMany 
	def student_names(self):
		return ', '.join([a.first_name for a in self.students.all()])
	student_names.short_description = "Student names"


	@property
	def done(self):
		count = len(self.group_user_set.all())
		if count > 1:
			for i, group in enumerate(self.group_user_set.all()):
				if not group.done:
					return False
				elif i + 1 == count:
					return True
		elif not self.group_user_set.all()[0].done:
			return False
		else:
			return True



	def __unicode__(self):
		return self.name


class Group_User(models.Model):
	group = models.ForeignKey(Group)
	student = models.ForeignKey(User, limit_choices_to= {'type':'student'})
	done = models.BooleanField(default = False)
	class Meta:
		unique_together = ("group", "student")
	def __unicode__(self):
		return self.group.name

	@property
	def score(self):
		sum = 0
		totalque = 0
		for que in self.group.evaluation.questions.all():
			for answer in que.answer_set.all():
				if answer.student_evaluated == self.student.id:
					sum += answer.score
					totalque += 1
		return str(sum) + '/' + str(totalque * 5)

	@property
	def check_user(self):
		return self.group.evaluation.questions.all()[0].answer_set.all().filter(student_evaluated = self.student.id)[0].student




	

