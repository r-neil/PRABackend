# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directtrains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_line', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='directtrain',
            name='train_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directtrains.TrainLine'),
        ),
    ]
