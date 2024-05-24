# Generated by Django 5.0.6 on 2024-05-24 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=55)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=55)),
                ('middle_name', models.CharField(blank=True, max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('age', models.IntegerField()),
                ('birth_date', models.DateTimeField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangocrudlesson.gender')),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
               
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
