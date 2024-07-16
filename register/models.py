from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title