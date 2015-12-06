# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0003_evaluation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_user',
            name='done',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
