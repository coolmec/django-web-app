from django.db import models

# Create your models here.
class Band(models.Model):
    name = models.fields.CharField(max_length = 100)


class Announce(models.Model):
    title = models.fields.CharField(max_length = 100)