from django.db import models
from .constants import ACCOUNT_TYPE_CHOICES
from django.contrib.auth.models import AbstractBaseUser
from .managers import AccountManager

# Create your models here.
class User(AbstractBaseUser):
	username = models.CharField(max_length=30, unique=True, blank= True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	type = models.CharField(max_length=20, choices= ACCOUNT_TYPE_CHOICES, default='student')
	email = models.EmailField(max_length=254, unique=True)
	student_number = models.CharField(max_length= 11, unique=True, null=True)
	is_superuser = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	objects = AccountManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username','first_name','last_name', ]
	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

	def has_perm(self, perm, obj=None):
		"""
		Returns True if user is an active superuser.
		"""
		if self.is_active and self.is_superuser:
			return True

	def has_perms(self, perm_list, obj=None):
		"""
		Returns True if the user has each of the specified permissions. If
		object is passed, it checks if the user has all required perms
		for this object.
		"""
		for perm in perm_list:
			if not self.has_perm(perm, obj):
				return False
		return True

	def has_module_perms(self, app_label):
		"""
		Returns True if user is an active superuser.
		"""
		if self.is_active and self.is_superuser:
			return True

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name


