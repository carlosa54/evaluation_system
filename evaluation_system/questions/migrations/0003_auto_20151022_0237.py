# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151021_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answered_by',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answered_for',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
