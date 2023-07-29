from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.views import (
    StudentsViewSet,
    TeachersViewSet,
    CoursesViewSet,
    EnrollmentViewSet,
    ListStudentEnrollment,
    ListEnrolledStudents
)

schema_view = get_schema_view(
    openapi.Info(
        title = 'RESTful API',
        default_version = 'v1',
        description = 'A RESTful API built with django',
        terms_of_service = '#',
        contact = openapi.Contact(email='example@domain.com'),
        license = openapi.License(name='BSD license'),
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
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
    path('api/docs', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema_swagger_ui'),
]
