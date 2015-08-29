from django.db import models
from .constants import ACCOUNT_TYPE_CHOICES
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class User(AbstractBaseUser):
	username = models.CharField(max_length=30, unique=True, blank= True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	type = models.CharField(max_length=20, choices= ACCOUNT_TYPE_CHOICES, default='student')
	email = models.EmailField(max_length=254, unique=True)
	student_number = models.CharField(max_length= 11, unique=True, null=True)
	is_superuser = models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name', ]
	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

class Group(models.Model):
	name = models.CharField(max_length=200)
	student = models.ManyToManyField(User)
