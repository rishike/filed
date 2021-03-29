# Generated by Django 3.1.7 on 2021-03-29 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audiobook',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('Narrator', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('upload_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('upload_time', models.DateTimeField(auto_now=True)),
                ('host', models.CharField(max_length=100)),
                ('participants', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.DurationField()),
                ('upload_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
