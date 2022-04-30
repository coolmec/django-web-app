from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Band(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)



class Announce(models.Model):

    class AnnounceType(models.TextChoices):
        RECORDS = "RECORDS"
        CLOTHING = "CLOTH"
        POSTERS = "POST"
        MISCELLANEOUS = "MISC"
    
    title = models.fields.CharField(max_length = 100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True, blank=True)
    announce_type = models.fields.CharField(choices=AnnounceType.choices, max_length=10)



    
    