from django.db import models

# Create your models here.


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to='pics')
    content = models.TextField(default="This is a sample text.")
    author = models.CharField(max_length = 30, default="Godwin Laureto")