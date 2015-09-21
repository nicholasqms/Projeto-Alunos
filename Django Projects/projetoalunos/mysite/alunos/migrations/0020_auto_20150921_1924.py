# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alunos', '0019_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orientador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nome do Orientador')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('register_number', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.CharField(default=b'your_email@service.com', max_length=100)),
                ('contact', models.PositiveIntegerField(null=True, blank=True)),
                ('CPF', models.PositiveIntegerField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='bolsa',
            field=models.CharField(default=b'PIBIC', max_length=7, choices=[(b'PIBIC', b'PIBIC'), (b'FAPERJ', b'FAPERJ'), (b'CNPq', b'CNPq'), (b'Projeto', b'Projeto')]),
        ),
    ]
