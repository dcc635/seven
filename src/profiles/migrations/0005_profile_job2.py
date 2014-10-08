# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job2',
            field=models.CharField(max_length=120, null=True),
            preserve_default=True,
        ),
    ]
