from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=30, blank=False, null=False, primary_key=True)
    rating = models.IntegerField(default=0)
    tier = models.CharField(max_length=15,blank=True, null=False)
