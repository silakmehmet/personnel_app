from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated


from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer
from .permissions import IsAdminOrReadOnly


class DepartmentMVS(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class PersonnelMVS(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
