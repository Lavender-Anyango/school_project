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
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('class_code', models.PositiveSmallIntegerField()),
                ('class_capacity', models.PositiveSmallIntegerField()),
                ('class_duration', models.TimeField()),
                ('class_training_assistant', models.CharField(max_length=20)),
                ('class_representative', models.CharField(max_length=20)),
                ('number_of_whiteboards', models.PositiveSmallIntegerField()),
                ('number_of_tables', models.PositiveSmallIntegerField()),
                ('number_of_chairs', models.PositiveSmallIntegerField()),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='teacher.teacher')),
            ],
        ),
    ]
