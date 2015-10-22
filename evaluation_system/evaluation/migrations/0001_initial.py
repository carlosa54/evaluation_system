# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.IntegerField()),
                ('seccion', models.CharField(max_length=3)),
                ('course', models.ForeignKey(to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation', models.ForeignKey(to='evaluation.Evaluation')),
                ('question', models.ForeignKey(to='questions.Question')),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='questions',
            field=models.ManyToManyField(to='questions.Question', through='evaluation.Evaluation_Question'),
        ),
    ]
