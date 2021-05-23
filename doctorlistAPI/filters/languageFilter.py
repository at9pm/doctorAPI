from ..models import Language
from django_filters import rest_framework as filters

class LanguageFilter(filters.FilterSet):
  class Meta:
    model = Language
    fields = {
      'language': ['iexact'],
    }
