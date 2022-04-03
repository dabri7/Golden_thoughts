from django.db import models


# Create your models here.
class Thought(models.Model):
    thought = models.TextField(null=False, blank=False, unique=True)
    author = models.CharField(max_length=128, blank=True, null=True)
