from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import DepartmentMVS, PersonnelMVS

router = DefaultRouter()
router.register("departments", DepartmentMVS)
router.register("personnels", PersonnelMVS)

urlpatterns = [

] + router.urls
