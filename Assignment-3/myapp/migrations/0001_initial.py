# Generated by Django 3.2.6 on 2021-08-15 05:25

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
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('college', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'student_info',
            },
        ),
    ]
