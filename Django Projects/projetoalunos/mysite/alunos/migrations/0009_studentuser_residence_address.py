# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0008_auto_20150914_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='residence_address',
            field=models.CharField(default=b'Insira o endereco de residencia', max_length=255),
        ),
    ]
