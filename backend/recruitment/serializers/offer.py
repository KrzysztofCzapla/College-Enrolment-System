from rest_framework import serializers

from recruitment.models import Offer


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ["id", "title", "description", "university", "max_number_of_students", "exams_requirements"]
