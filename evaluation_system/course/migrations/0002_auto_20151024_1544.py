# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_user',
            old_name='proffesor',
            new_name='professor',
        ),
        migrations.RemoveField(
            model_name='course',
            name='proffesor',
        ),
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.ManyToManyField(related_name='professor', through='course.Course_User', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
