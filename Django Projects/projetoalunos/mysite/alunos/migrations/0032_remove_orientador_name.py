# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0031_auto_20150922_1213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orientador',
            name='name',
        ),
    ]
