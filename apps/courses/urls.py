from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, ChapterViewSet, LessonViewSet, EnrollmentViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'chapters', ChapterViewSet, basename='chapter')
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollments')

urlpatterns = [
    path('', include(router.urls)),
]
