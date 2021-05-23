from ..models import Doctor
from django_filters import rest_framework as filters


class DoctorFilter(filters.FilterSet):
  class Meta:
    model = Doctor
    fields = {
      'district': ['iexact'],
    }
