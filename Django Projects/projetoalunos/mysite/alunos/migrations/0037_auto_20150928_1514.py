# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alunos.models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0036_student_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=b'example@lps.ufrj.br', max_length=254),
        ),
        migrations.AlterField(
            model_name='student',
            name='DRE',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[alunos.models.dre_is_valid]),
        ),
    ]
