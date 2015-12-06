# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20151105_0007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answers',
        ),
        migrations.AddField(
            model_name='answer',
            name='evaluation_id',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questions.Question', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='student_evaluated',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set([('question', 'evaluation_id', 'student', 'student_evaluated')]),
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answered_for',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answered_by',
        ),
    ]
