from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Personnel(models.Model):
    TITLE = (
        (1, "Team Lead"),
        (2, "Mid Lead"),
        (3, "Junior")
    )

    GENDER = (
        (1, "Male"),
        (2, "Female")
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.PositiveSmallIntegerField(choices=TITLE, default=3)
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=2)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="personnel")
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.title}"
