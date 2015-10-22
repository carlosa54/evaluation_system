# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangoyearlessdate.models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='academic_year',
            field=djangoyearlessdate.models.YearField(default=b'2015'),
        ),
    ]
