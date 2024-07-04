from django.contrib.auth import get_user_model
from rest_framework import serializers

from recruitment.models import Exam


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ["id", "name", "owner", "score"]
