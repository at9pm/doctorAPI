from ..models import Service
from django_filters import rest_framework as filters

class ServiceFilter(filters.FilterSet):
  class Meta:
    model = Service
    fields = {
      'serviceType': ['iexact'],
      'price': ['gte', 'lte'],
    }
