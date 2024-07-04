from rest_framework import viewsets, permissions

from recruitment.serializers.exam import ExamSerializer


class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.exams.all()
