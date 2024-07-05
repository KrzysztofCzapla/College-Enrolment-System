from recruitment.models import OfferStage
from rest_framework import serializers
from datetime import datetime


class CustomDateTimeField(serializers.DateTimeField):
    def to_representation(self, value):
        if not value:
            return None
        return value.strftime('%Y-%m-%d %H:%M')

    def to_internal_value(self, data):
        try:
            return datetime.strptime(data, '%Y-%m-%d %H:%M')
        except ValueError:
            self.fail('invalid', format='YYYY-MM-DD HH:MM')


class OfferStageSerializer(serializers.ModelSerializer):
    start_date = CustomDateTimeField()
    end_date = CustomDateTimeField()

    class Meta:
        model = OfferStage
        fields = ["id", "offer", "start_date", "end_date"]


