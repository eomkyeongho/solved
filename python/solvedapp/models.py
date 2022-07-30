from django.db import models

# Create your models here.
class Solvedapp(models.Model):
    name = models.CharField('NAME', max_length=5, blank=True)
    todo = models.CharField('TODO', max_length=50)

    def __str__(self):
        return self.todo

# 아마 DB 구조인듯?