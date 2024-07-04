from rest_framework import viewsets, permissions

from recruitment.serializers.offer_stage import OfferStageSerializer


class OfferStageViewSet(viewsets.ModelViewSet):
    serializer_class = OfferStageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.offerstages.all()
