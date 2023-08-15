from django.db import models

# Create your models here.
class talk(models.Model):
    content = models.TextField()