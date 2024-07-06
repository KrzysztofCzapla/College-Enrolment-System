from rest_framework import viewsets, permissions

from recruitment.models import Exam
from recruitment.serializers.exams_group import ExamsGroupSerializer
from accounts.enums import AccountTypes
from accounts.permissions import IsStudent


class ExamsGroupViewSet(viewsets.ModelViewSet):
    serializer_class = ExamsGroupSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [IsStudent(), ]
        else:
            return [permissions.IsAuthenticated(), ]

    def get_queryset(self):
        if self.request.user.account_type != AccountTypes.ADMIN:
            return self.request.user.exams.all()
        else:
            return Exam.objects.all()
