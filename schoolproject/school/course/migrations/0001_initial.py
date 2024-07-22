# Generated by Django 5.0.7 on 2024-07-12 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_title', models.CharField(max_length=20)),
                ('course_category', models.CharField(max_length=20)),
                ('course_start_date', models.DateField()),
                ('course_end_date', models.DateField()),
                ('course_code', models.PositiveSmallIntegerField()),
                ('maximum_attendees', models.PositiveSmallIntegerField()),
                ('course_level', models.CharField(max_length=20)),
                ('course_fee', models.PositiveSmallIntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='teacher.teacher')),
            ],
        ),
    ]