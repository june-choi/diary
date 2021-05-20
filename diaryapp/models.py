from django.db import models

# Create your models here.
class Diaryapp(models.Model) :
    title = models.CharField(max_length=500)
    body = models.TextField()