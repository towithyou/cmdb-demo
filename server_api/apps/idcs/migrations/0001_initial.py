# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-05 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='机房名称')),
                ('address', models.CharField(max_length=256, verbose_name='机房地址')),
                ('phone', models.CharField(max_length=15, verbose_name='联系人')),
                ('email', models.EmailField(default=None, max_length=254, verbose_name='邮件地址')),
                ('letter', models.CharField(max_length=5, verbose_name='IDC简称')),
            ],
            options={
                'db_table': 'resources_idc',
            },
        ),
    ]
