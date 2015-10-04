# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alunos.models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0051_auto_20151004_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DRE',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[alunos.models.dre_is_valid]),
        ),
    ]
