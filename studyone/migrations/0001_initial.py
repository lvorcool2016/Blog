# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-31 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('context', models.TextField(null=True)),
                ('createOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usersname', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, '保密')])),
                ('createOn', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ManyToManyField(to='studyone.users'),
        ),
    ]