# Generated by Django 5.0.7 on 2024-07-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('student_code', models.PositiveSmallIntegerField()),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=20)),
                ('bio', models.TextField()),
                ('age', models.PositiveSmallIntegerField()),
                ('phone_number', models.CharField(max_length=20)),
                ('immediate_contact', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('classes', models.ManyToManyField(related_name='students', to='classroom.classroom')),
                ('courses', models.ManyToManyField(related_name='students', to='course.course')),
            ],
        ),
    ]
