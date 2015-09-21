# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0007_teacheruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='rg',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='telephone_number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='zip_code',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
