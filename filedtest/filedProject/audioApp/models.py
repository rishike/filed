from django.db import models
from django.core.exceptions import ValidationError

def validate_participants(value):
    name_list = list(map(str, value.split(',')))
    check_length = [False for v in name_list if len(v) > 100]
    if len(name_list) > 10 or False in check_length :
        raise ValidationError("Participants Field value should be comma separated and \
each string cannot be larger than 100 characters, maximum of 10 participants possible")
    return value

# Create your models here.

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    upload_time = models.DateTimeField(auto_now=True)
    file_url = models.CharField(max_length=250, blank=True)

class Podcast(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    upload_time = models.DateTimeField(auto_now=True)
    host = models.CharField(max_length=100)
    participants = models.TextField(blank=True, validators=[validate_participants])
    file_url = models.CharField(max_length=250, blank=True)



class Audiobook(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    upload_time = models.DateTimeField(auto_now=True)
    file_url = models.CharField(max_length=250, blank=True)