# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20151105_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answered_by',
            field=models.ForeignKey(related_name='answered_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answered_for',
            field=models.ForeignKey(related_name='answered_for', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ForeignKey(blank=True, to='questions.Answer', null=True),
            preserve_default=True,
        ),
    ]
