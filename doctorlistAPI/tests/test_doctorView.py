from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from ..models import *


class TestDoctorView(APITestCase):

# prepare common objects required for test cases
  def setUp(self):
    self.doctor1 = Doctor.objects.create(
      doctorID = "HK0001",
      name = "doctor1",
      contactNumber = "12345678",
      address = "test address",
      openingHours = "opening from 9 to 6",
      district = "HK"
    )
    self.doctor2 = Doctor.objects.create(
      doctorID = "HK0002",
      name = "doctor2",
      contactNumber = "12345678",
      address = "test address",
      openingHours = "opening from 9 to 6",
      district = "KL"
    )
    self.doctor3 = Doctor.objects.create(
      doctorID = "HK0003",
      name = "doctor3",
      contactNumber = "12345678",
      address = "test address",
      openingHours = "opening from 9 to 6",
      district = "HK"
    )
    self.doctor1service1 = Service.objects.create(
      serviceType = 'PHY',
      doctor = self.doctor1,
      price = 300
    )
    self.doctor1service2 = Service.objects.create(
      serviceType = 'CLN',
      doctor = self.doctor1,
      price = 30
    )
    self.doctor2service1 = Service.objects.create(
      serviceType = 'CHN',
      doctor = self.doctor2,
      price = 100
    )
    self.doctor3service1 = Service.objects.create(
      serviceType = 'CLN',
      doctor = self.doctor3,
      price = 200
    )
    self.doctor1Language1 = Language.objects.create(
      doctor = self.doctor1,
      language = 'CNT'
    )
    self.doctor1Language2 = Language.objects.create(
      doctor = self.doctor1,
      language = 'ENG'
    )
    self.doctor2Language1 = Language.objects.create(
      doctor = self.doctor2,
      language = 'CNT'
    )
    self.doctor2Language2 = Language.objects.create(
      doctor = self.doctor2,
      language = 'MDR'
    )
    self.doctor3Language1 = Language.objects.create(
      doctor = self.doctor3,
      language = 'CNT'
    )

    self.allDoctors = Doctor.objects.all()
    self.allService = Service.objects.all()
    self.allLanguage = Language.objects.all()

  def test_doctor_list_can_return_all_doctors(self):
    listAllDoctorsUrl = reverse('doctor-list')
    response = self.client.get(listAllDoctorsUrl)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), self.allDoctors.count())

  def test_doctor_detail_returns_specified_doctor(self):
    doctorDetailUrl = reverse('doctor-detail', kwargs={"pk": 1})
    singleDoctor = Doctor.objects.get(doctorID=self.doctor1.doctorID)
    response = self.client.get(doctorDetailUrl)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data["doctorID"], singleDoctor.doctorID)

  def test_doctor_list_can_filter_district(self):
    filterHKDoctorsUrl = "/doctor/?district=HK"
    returnDoctors = self.allDoctors.filter(district="HK")
    response = self.client.get(filterHKDoctorsUrl)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), returnDoctors.count())

  def test_doctor_list_can_filter_language(self):
    filterCantoneseDoctorsUrl = "/doctor/?language=CNT"
    returnlanguage = self.allLanguage.filter(language="CNT")
    response = self.client.get(filterCantoneseDoctorsUrl)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), returnlanguage.count())

  def test_doctor_list_can_filter_category(self):
    filterClinicDoctorsUrl = "/doctor/?category=CLN"
    returnService = self.allService.filter(serviceType="CLN")
    response = self.client.get(filterClinicDoctorsUrl)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), returnService.count())

  def test_doctor_list_can_filter_price(self):
    filterDesiredPriceDoctorsUrl = "/doctor/?price_range=0,200"
    returnService = self.allService.filter(price__range=(0, 200))
    returnDoctor = set()
    for service in returnService:
      returnDoctor.add(service.doctor.doctorID)
    response = self.client.get(filterDesiredPriceDoctorsUrl)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), len(returnDoctor))
