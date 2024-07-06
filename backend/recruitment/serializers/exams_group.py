from django.contrib.auth import get_user_model
from rest_framework import serializers

from recruitment.models.exams_group import ExamsGroup


class ExamsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamsGroup
        fields = ["id", "owner", "exams"]
