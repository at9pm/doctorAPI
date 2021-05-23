from django.db import models

class Doctor(models.Model):
  
# django way of enum
  class DistrictChoice(models.TextChoices):
    KOWLOON = 'KL'
    HONG_KONG = 'HK'
    ISLAND = 'IL'
    NEW_TERRITORIES = 'NT'
  
# attributes
  doctorID = models.CharField(max_length=6, unique=True)
  name = models.CharField(max_length=200)
  contactNumber = models.CharField(max_length=32, null=True)
  address = models.CharField(max_length=500, null=True)
  openingHours = models.CharField(max_length=100, null=True)
  district = models.CharField(
        max_length = 2,
        choices = DistrictChoice.choices,
    )
  
  def __str__(self):
    return self.doctorID 