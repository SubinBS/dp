from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    # If you want a 'description' field, it should be defined here
    description = models.TextField(blank=True, null=True)
