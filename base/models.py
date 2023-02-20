from django.db import models

# Create your models here.


class Book(models.Model):
    book_id = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=255)
    language = models.CharField(max_length=255, blank=True, null=True)
    copyright = models.BooleanField()
