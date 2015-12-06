# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(default=b'student', max_length=20, choices=[(b'professor', b'professor'), (b'student', b'student')]),
            preserve_default=True,
        ),
    ]
