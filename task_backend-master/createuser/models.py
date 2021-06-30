from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import datetime

# Create your models here.
class assignTaskFiles(models.Model):
    File_Name = models.TextField(null=True, blank=True)
    Task_level = models.TextField(null=True, blank=True)
    Priority = models.TextField(null=True, blank=True)
    Created_Date = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    Action =models.TextField(null=True, blank=True)

class loginprofile(models.Model):
    firstName = models.TextField(null=True, blank=True)
   # lastname = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    role = models.TextField( blank=True)

class objectLevel(models.Model):
    trackId = models.TextField(null=True, blank=True)
    objectClass =models.TextField(null=True, blank=True)
    occlusion =models.TextField(null=True, blank=True)
    pose =models.TextField(null=True, blank=True)
    lane_change =models.BooleanField(null=True, blank=True)
    breakLight=models.BooleanField(null=True, blank=True)


class SceneLevel(models.Model):
    Light_Condition = models.TextField(null=True, blank=True)
    Road_Type =models.TextField(null=True, blank=True)
    Road_works =models.TextField(null=True, blank=True)
    Tunnel =models.TextField(null=True, blank=True)
    Weather =models.TextField(null=True, blank=True)
    Street_Condition =models.TextField(null=True, blank=True)
    

    # Create your models here.
class userprofile(models.Model):
    firstName = models.TextField(null=True, blank=True)
   # lastname = models.TextField(null=True, blank=True)
    password = models.TextField(null=True, blank=True)
    role = models.TextField( blank=True)