from django.db import models
from googletrans import Translator
# Create your models here.

class Trans(models.Model):
    source = models.TextField()
    destination = models.TextField()