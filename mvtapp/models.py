from django.db import models

# Create your models here.

class LectureDetail(models.Model):
    objects = None  #views.py에서 line 35 else 부분에 objects
    title = models.CharField(max_length=255, null=False)
    person = models.CharField(max_length=255, null=False)
    meeting = models.CharField(max_length=255, null=False)
