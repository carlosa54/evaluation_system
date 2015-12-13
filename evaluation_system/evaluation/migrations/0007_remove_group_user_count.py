# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0006_group_user_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_user',
            name='count',
        ),
    ]
