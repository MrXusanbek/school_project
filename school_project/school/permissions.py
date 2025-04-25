from rest_framework.permissions import BasePermission

class IsTeacher(BasePermission):
    """
    Faqat Teacher bo‘lsa ruxsat beriladi
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'teacher'


class IsStudent(BasePermission):
    """
    Faqat Student bo‘lsa ruxsat beriladi
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == 'student'
