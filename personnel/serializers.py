from rest_framework import serializers

from .models import Department, Personnel


class DepartmentSerializer(serializers.ModelSerializer):
    personnel_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = "__all__"
        read_only_fields = ("id",)

    def get_personnel_count(self, obj):
        return obj.personnel_set.count()


class PersonnelSerializer(serializers.ModelSerializer):
    department_name = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        fields = "__all__"
        read_only_fields = ("id",)

    def get_department_name(self, obj):
        return obj.department.name
