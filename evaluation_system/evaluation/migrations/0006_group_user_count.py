# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0005_evaluation_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_user',
            name='count',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
