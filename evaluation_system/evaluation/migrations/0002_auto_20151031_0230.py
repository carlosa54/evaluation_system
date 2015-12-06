# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='students',
            field=models.ManyToManyField(related_name='group', through='evaluation.Group_User', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
