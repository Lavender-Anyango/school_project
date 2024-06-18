# Generated by Django 5.0.6 on 2024-06-18 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=20)),
                ('course_objective', models.CharField(max_length=20)),
                ('course_duration', models.DurationField()),
                ('course_students', models.CharField(max_length=20)),
                ('course_level', models.PositiveSmallIntegerField()),
                ('course_description', models.TextField(max_length=30)),
                ('course_title', models.CharField(max_length=10)),
                ('course_teacher', models.CharField(max_length=15)),
                ('course_id', models.PositiveSmallIntegerField()),
                ('course_resources', models.CharField(max_length=19)),
            ],
        ),
    ]