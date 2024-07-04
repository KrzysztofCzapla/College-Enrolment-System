from rest_framework import serializers

from recruitment.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "student", "university", "offer", "offer_stage", "priority", "exams"]
