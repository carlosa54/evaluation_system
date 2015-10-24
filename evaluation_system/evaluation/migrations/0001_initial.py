# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangoyearlessdate.models


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
                ('academic_year', djangoyearlessdate.models.YearField(default=b'2015')),
                ('semester', models.IntegerField()),
                ('seccion', models.CharField(max_length=3)),
                ('course', models.ForeignKey(to='course.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Evaluation_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('evaluation', models.ForeignKey(to='evaluation.Evaluation')),
                ('question', models.ForeignKey(to='questions.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='evaluation',
            name='questions',
            field=models.ManyToManyField(to='questions.Question', through='evaluation.Evaluation_Question'),
            preserve_default=True,
        ),
    ]
