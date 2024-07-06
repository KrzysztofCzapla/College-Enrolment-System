from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from accounts.enums import AccountTypes
from accounts.permissions import IsStaff
from recruitment.models import OfferStage
from recruitment.serializers.offer_stage import OfferStageSerializer
from recruitment.tasks import calculate_stage_results, confirm_stage


class OfferStageViewSet(viewsets.ModelViewSet):
    serializer_class = OfferStageSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [
                IsStaff(),
            ]
        else:
            return [
                permissions.IsAuthenticated(),
            ]

    def get_queryset(self):
        if self.request.user.account_type != AccountTypes.ADMIN:
            return self.request.user.offer_stages.all()
        else:
            return OfferStage.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        stage_end_date = serializer.instance.end_date
        stage_confirmation_date = serializer.instance.end_date
        stage_id = serializer.instance.id

        calculate_stage_results.apply_async(
            eta=stage_end_date, kwargs={"stage_id": stage_id}
        )
        confirm_stage.apply_async(
            eta=stage_confirmation_date, kwargs={"stage_id": stage_id}
        )

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
