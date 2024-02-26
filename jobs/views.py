from django.shortcuts import render
from rest_framework import viewsets
from . models import jobCategoryModel,jobCircularModel,jobApplicationModel
from . serializer import jobCategorySerializer,jobCircularSerializer,jobApplicationSerializer

# Create your views here.
class jobCategoryViewset(viewsets.ModelViewSet):
    queryset = jobCategoryModel.objects.all()
    serializer_class = jobCategorySerializer


class jobCircularViewset(viewsets.ModelViewSet):
    queryset = jobCircularModel.objects.all()
    serializer_class = jobCircularSerializer


class jobApplicationViewset(viewsets.ModelViewSet):
    queryset = jobApplicationModel.objects.all()
    serializer_class = jobApplicationSerializer