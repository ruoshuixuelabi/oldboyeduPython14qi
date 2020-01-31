# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-02-27 01:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_type', models.SmallIntegerField(default=0)),
                ('name', models.TextField()),
                ('order', models.SmallIntegerField(default=0, verbose_name='用于排序字段')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Tag'),
        ),
    ]
