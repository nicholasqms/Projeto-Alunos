# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0020_auto_20150921_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='bolsa',
            field=models.CharField(default=b'PIBIC', max_length=7, choices=[(b'PIBIC', b'PIBIC'), (b'FAPERJ', b'FAPERJ'), (b'CNPq', b'CNPq'), (b'Projeto', b'Projeto')]),
        ),
    ]
