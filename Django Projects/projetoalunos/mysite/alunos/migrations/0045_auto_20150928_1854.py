# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0044_auto_20150928_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='data_Nascimento',
            field=models.DateField(default=b'2001-01-01', blank=True),
        ),
    ]
