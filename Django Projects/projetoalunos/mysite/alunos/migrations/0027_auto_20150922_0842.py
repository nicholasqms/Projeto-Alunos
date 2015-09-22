# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0026_auto_20150922_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='dre',
            new_name='DRE',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='rg',
            new_name='RG',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='dre',
            new_name='DRE',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='rg',
            new_name='RG',
        ),
    ]
