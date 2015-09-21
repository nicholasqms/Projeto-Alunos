# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alunos', '0018_auto_20150915_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b"Student's Name")),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('dre', models.PositiveIntegerField(null=True, blank=True)),
                ('rg', models.PositiveIntegerField(null=True, blank=True)),
                ('zip_code', models.PositiveIntegerField(null=True, blank=True)),
                ('residence_address', models.CharField(default=b'Insira o endereco de residencia', max_length=255)),
                ('telephone_number', models.PositiveIntegerField(null=True, blank=True)),
                ('course', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
