# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-11 02:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0002_auto_20190907_0427'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'ordering': ['id'], 'permissions': (('view_server', 'can view server 查看get'),)},
        ),
    ]
