# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0045_auto_20150928_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='numero_agencia',
            field=models.PositiveIntegerField(null=True, verbose_name=b'N\xc3\xbamero Ag\xc3\xaancia', blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='numero_conta',
            field=models.PositiveIntegerField(null=True, verbose_name=b'N\xc3\xbamero Conta', blank=True),
        ),
    ]
