# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answered_for',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answered_by',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
