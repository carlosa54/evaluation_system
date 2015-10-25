# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ForeignKey(to='questions.Answer', null=True),
            preserve_default=True,
        ),
    ]
