# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20151025_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answered_by',
            field=models.ForeignKey(related_name='answered_by', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answered_for',
            field=models.ForeignKey(related_name='answered_for', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
