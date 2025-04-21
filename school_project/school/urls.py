from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClassViewSet, TeacherViewSet, StudentViewSet, home

router = DefaultRouter()
router.register(r'classes', ClassViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


router = DefaultRouter()
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('', home),
    path('', include(router.urls)),
]
