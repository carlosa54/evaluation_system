# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0002_auto_20151031_0230'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='name',
            field=models.CharField(default=b'Unknown', max_length=200),
            preserve_default=True,
        ),
    ]
