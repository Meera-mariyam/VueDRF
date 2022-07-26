from unicodedata import name
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    rating = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name