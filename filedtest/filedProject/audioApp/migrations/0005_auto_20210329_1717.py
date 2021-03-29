# Generated by Django 3.1.7 on 2021-03-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audioApp', '0004_auto_20210329_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiobook',
            name='file_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='podcast',
            name='file_url',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='song',
            name='file_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]