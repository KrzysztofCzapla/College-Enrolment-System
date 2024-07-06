from rest_framework import permissions, viewsets

from accounts.enums import AccountTypes
from accounts.permissions import IsStudent
from recruitment.models import Exam
from recruitment.serializers.exam import ExamSerializer


class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "delete"]:
            return [
                IsStudent(),
            ]
        else:
            return [
                permissions.IsAuthenticated(),
            ]

    def get_queryset(self):
        if self.request.user.account_type != AccountTypes.ADMIN:
            return self.request.user.exams.all()
        else:
            return Exam.objects.all()
