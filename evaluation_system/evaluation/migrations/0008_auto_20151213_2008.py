# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0007_remove_group_user_count'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='group_user',
            unique_together=set([('group', 'student')]),
        ),
    ]
