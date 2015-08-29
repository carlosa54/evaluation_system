from django.conf import settings
from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):

    def create_user(self, username, email, first_name, last_name, type,
                    password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            type=type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name,
                         password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            type='proffesor',
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user