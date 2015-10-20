# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20150829_0432'),
        ('users', '0004_user_is_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='student',
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
