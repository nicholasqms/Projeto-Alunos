# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0040_studentstatus_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='passaporte_numero',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
