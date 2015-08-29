# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('section', models.CharField(max_length=3)),
                ('groups', models.ManyToManyField(to='users.Group')),
                ('proffesor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('questions', models.ManyToManyField(to='questions.Question')),
            ],
        ),
    ]
