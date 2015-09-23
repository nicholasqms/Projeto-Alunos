# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0035_auto_20150922_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(default=b'Ativo', max_length=30, choices=[(b'Ativo', b'Ativo'), (b'Inativo', b'Inativo'), (b'Viajando', b'Viajando')]),
        ),
    ]
