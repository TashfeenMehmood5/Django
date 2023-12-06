# Generated by Django 4.2.6 on 2023-10-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('student_email', models.EmailField(max_length=254)),
                ('student_course', models.CharField(max_length=50)),
                ('student_progress', models.TextField()),
            ],
        ),
    ]
