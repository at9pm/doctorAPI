from .doctor import Doctor
from django.db import models

class Service(models.Model):
  
# django way of enum
  class ServiceChoice(models.TextChoices):
    PHYSIO = 'PHY'
    DENTAL = 'DEN'
    CHINMED = 'CHN'
    CLINIC = 'CLN'

# attributes
  doctor = models.ForeignKey(
    Doctor,
    on_delete = models.CASCADE
  )
  serviceType = models.CharField(
        max_length = 3,
        choices = ServiceChoice.choices,
  )
  price = models.DecimalField(
    max_digits = 10,
    decimal_places = 2,
    default = 0.0
  )

# avoid duplicate
  class Meta:
    unique_together = ["doctor", "serviceType"]