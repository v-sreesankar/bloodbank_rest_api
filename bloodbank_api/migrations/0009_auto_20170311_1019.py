# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-03-11 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank_api', '0008_remove_donerdetails_coordinates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donerdetails',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
