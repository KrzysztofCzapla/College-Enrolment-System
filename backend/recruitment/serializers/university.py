from rest_framework import serializers

from recruitment.models import University


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ["id", "name", "owner", "address", "confirmed_students"]
