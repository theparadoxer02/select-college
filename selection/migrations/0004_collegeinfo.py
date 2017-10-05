# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-05 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0003_auto_20171005_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.CharField(max_length=10)),
                ('average_salary', models.CharField(max_length=100)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selection.College')),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='selection.Courses')),
            ],
        ),
    ]
