from rest_framework import serializers

from recruitment.models import Offer


class ExamsRequirementsSerializer(serializers.Serializer):
    exams = serializers.ListField(child=serializers.CharField())
    weight = serializers.FloatField()


class OfferSerializer(serializers.ModelSerializer):
    exams_requirements = serializers.ListField(child=ExamsRequirementsSerializer())

    class Meta:
        model = Offer
        fields = ["id", "title", "description", "university", "max_number_of_students", "exams_requirements", "confirmed_students", "is_open"]
