from django.urls import path

from rest_framework.authtoken import views

from .views import RegisterCreateAPIView

urlpatterns = [
    path("register/", RegisterCreateAPIView.as_view()),
    path('login/', views.obtain_auth_token),
]
