from rest_framework import serializers

from recruitment.models import OfferStage


class OfferStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferStage
        fields = ["id", "offer", "start_date", "end_date"]

    
