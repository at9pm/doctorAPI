from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from ..serializers import DoctorSerializer
from ..models import Doctor
from ..models import Language
from ..models import Service
from ..filters.doctorFilter import DoctorFilter
from django.db.models import Exists, OuterRef



class DoctorViewSet(viewsets.ModelViewSet):
  queryset = Doctor.objects.all()
  filterset_class = DoctorFilter
  serializer_class = DoctorSerializer

# define a new customized list view to override to the django one
  def list(self, request):

# get the request parameters
    district = self.request.GET.get('district')
    category = self.request.GET.get('category')
    price_range = self.request.GET.get('price_range')
    language = self.request.GET.get('language')

# first get all doctors
    returnDoctor = Doctor.objects.all()

# then filter each criteria one by one if it is specified in the request
    if district != None:
      returnDoctor = returnDoctor.filter(district=district)
    
    if language != None:
      desiredLanguage = Language.objects.filter(language=language)
      returnDoctor = returnDoctor.filter(
        Exists(desiredLanguage.filter(doctor=OuterRef('pk')))
      ).distinct()

    if category != None:
      desiredService = Service.objects.filter(serviceType=category)
      returnDoctor = returnDoctor.filter(
        Exists(desiredService.filter(doctor=OuterRef('pk')))
      ).distinct()

    if price_range != None:
      lowPrice = price_range.split(",")[0]
      highPrice = price_range.split(",")[1]
      desiredService = Service.objects.filter(price__gte=lowPrice, price__lte=highPrice)
      returnDoctor = returnDoctor.filter(
        Exists(desiredService.filter(doctor=OuterRef('pk')))
      ).distinct()

# special handle this case as price and category belongs to the same Service model
    if (category != None) and (price_range != None):
      desiredService = desiredService.filter(serviceType=category, price__gte=lowPrice, price__lte=highPrice)
      returnDoctor = returnDoctor.filter(
        Exists(desiredService.filter(doctor=OuterRef('pk')))
      ).distinct()
      print(desiredService)

# return the result
    serializer = DoctorSerializer(returnDoctor, many=True)
    return Response(serializer.data)