from .doctor import Doctor
from django.db import models

class Language(models.Model):
  
# django way of enum
  class LanguageChoice(models.TextChoices):
    CANTONESE = 'CNT'
    MANDARIN = 'MDR'
    ENGLISH = 'ENG'
  
# attributes
  doctor = models.ForeignKey(
    Doctor,
    on_delete = models.CASCADE
  )
  language = models.CharField(
        max_length = 3,
        choices = LanguageChoice.choices,
  )

# avoid duplicate
  class Meta:
    unique_together = ["doctor", "language"]