from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Task(models.Model):
    first = models.CharField(max_length = 50)

    def __str__(self):
        return self.first