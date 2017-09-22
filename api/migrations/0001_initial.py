# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-22 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TiposAtributos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=5, unique=True)),
                ('descripcion', models.CharField(blank=True, default='', max_length=100)),
                ('creado', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('codigo',),
            },
        ),
    ]
