from rest_framework import permissions

from accounts.enums import AccountTypes


class IsStudent(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        user_type = getattr(request.user, "account_type")

        return user_type in (AccountTypes.STUDENT, AccountTypes.ADMIN)


class IsStaff(permissions.IsAuthenticated):

    def has_permission(self, request, view):
        user_type = getattr(request.user, "account_type")

        return user_type in (AccountTypes.UNIVERSITY_STAFF, AccountTypes.ADMIN)