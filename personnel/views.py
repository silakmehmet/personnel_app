from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer


class DepartmentMVS(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonnelMVS(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
