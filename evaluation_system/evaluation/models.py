from django.db import models
from djangoyearlessdate.models import YearField
from ..questions.models import Question
from ..course.models import Course
# Create your models here.
class Evaluation(models.Model):
	academic_year = YearField(default = '2015')
	course = models.ForeignKey(Course)
	semester = models.IntegerField()
	seccion = models.CharField(max_length= 3)
	questions = models.ManyToManyField(Question, through = "Evaluation_Question")

class Evaluation_Question(models.Model):
	evaluation = models.ForeignKey(Evaluation)
	question = models.ForeignKey(Question)

