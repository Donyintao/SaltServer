# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-23 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faults', '0002_auto_20190123_1651'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='faultsclass',
            table='faults_class',
        ),
        migrations.AlterModelTable(
            name='faultscontent',
            table='faults_content',
        ),
    ]
