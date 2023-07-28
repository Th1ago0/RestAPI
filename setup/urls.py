from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import (
    StudentsViewSet,
    TeachersViewSet,
    CoursesViewSet,
    EnrollmentViewSet,
    ListStudentEnrollment,
    ListEnrolledStudents
)

router = routers.DefaultRouter()
router.register('alunos', StudentsViewSet, basename = 'Students')
router.register('cursos',CoursesViewSet, basename = 'Courses')
router.register('matriculas', EnrollmentViewSet, basename = 'Enrollments')
router.register('professores', TeachersViewSet, basename = 'Teachers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/alunos/<int:pk>/matriculas', ListStudentEnrollment.as_view()),
    path('api/cursos/<int:pk>/matriculas', ListEnrolledStudents.as_view()),
]
