from rest_framework import viewsets
from .models import Class, Teacher, Student
from .serializers import ClassSerializer, TeacherSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


@api_view(['GET'])
def home(request):
    return Response({
        "message": "Welcome to the School Project API 🎓",
        "endpoints": {
            "Teachers": "/api/teachers/",
            "Students": "/api/students/",
            "Classes": "/api/classes/",
            "JWT Token": "/api/token/",
            "Swagger docs": "/swagger/",
        }
    })



