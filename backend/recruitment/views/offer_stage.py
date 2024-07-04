from rest_framework import viewsets, permissions

from accounts.enums import AccountTypes
from accounts.permissions import IsStaff
from recruitment.models import OfferStage
from recruitment.serializers.offer_stage import OfferStageSerializer


class OfferStageViewSet(viewsets.ModelViewSet):
    serializer_class = OfferStageSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsStaff(), ]
        else:
            return [permissions.IsAuthenticated(), ]

    def get_queryset(self):
        if self.request.user.account_type != AccountTypes.ADMIN:
            return self.request.user.offer_stages.all()
        else:
            return OfferStage.objects.all()
