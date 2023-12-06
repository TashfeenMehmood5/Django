# Generated by Django 4.2.6 on 2023-12-02 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(upload_to='uploaded_images')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
