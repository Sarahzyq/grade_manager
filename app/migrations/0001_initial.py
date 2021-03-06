# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 11:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cid', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=20)),
                ('learnhours', models.FloatField()),
                ('credit', models.FloatField()),
                ('precourse', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('scholarship_level', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('money', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Selectcourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.FloatField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.IntegerField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('classes', models.CharField(max_length=20)),
                ('birthpalce', models.CharField(max_length=20)),
                ('scholarship_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Scholarship')),
            ],
        ),
        migrations.AddField(
            model_name='selectcourse',
            name='sid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Student'),
        ),
        migrations.AlterUniqueTogether(
            name='selectcourse',
            unique_together=set([('sid', 'cid')]),
        ),
    ]
