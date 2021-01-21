from django.db import models


class Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=80)
    subject = models.CharField(max_length=90)
    message = models.TextField()
