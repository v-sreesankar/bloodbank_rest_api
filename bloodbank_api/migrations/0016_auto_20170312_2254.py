# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-12 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank_api', '0015_auto_20170311_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donerdetails',
            name='coordinates3',
        ),
        migrations.AddField(
            model_name='donerdetails',
            name='district',
            field=models.TextField(default='Trivandrum', max_length=100),
        ),
    ]