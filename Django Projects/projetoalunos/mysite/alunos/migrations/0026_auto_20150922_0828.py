# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0025_auto_20150922_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='telephone_number',
            new_name='CEP',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='course',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='residence_address',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='zip_code',
            new_name='telefone',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='telephone_number',
            new_name='CEP',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='course',
            new_name='curso',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='residence_address',
            new_name='endereco',
        ),
        migrations.RenameField(
            model_name='studentuser',
            old_name='zip_code',
            new_name='telefone',
        ),
    ]
