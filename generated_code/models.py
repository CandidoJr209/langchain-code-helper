from django.db import models

class House(models.Model):
    address = models.CharField(max_length=255)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    year_built = models.IntegerField()
    lot_size = models.IntegerField()
    heating_type = models.CharField(max_length=255)
    cooling_type = models.CharField(max_length=255)
    garage_type = models.CharField(max_length=255)
    pool = models.BooleanField()