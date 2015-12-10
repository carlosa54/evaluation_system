# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0004_group_user_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='created_by',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
