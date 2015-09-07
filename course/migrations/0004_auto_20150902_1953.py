# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='student',
            new_name='students',
        ),
    ]
