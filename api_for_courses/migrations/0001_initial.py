# Generated by Django 4.1 on 2023-09-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=300)),
                ('Course_code', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='course_instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.CharField(max_length=10)),
                ('Semester', models.CharField(max_length=10)),
                ('Course_id', models.CharField(max_length=10)),
            ],
        ),
    ]