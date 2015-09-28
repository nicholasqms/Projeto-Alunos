# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0043_auto_20150928_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBolsa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'PIBIC', max_length=255, verbose_name=b'Tipo de Bolsa')),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='bolsa',
            field=models.ForeignKey(verbose_name=b'Bolsa', to='alunos.StudentBolsa'),
        ),
    ]
