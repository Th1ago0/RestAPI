from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import (
    Student,
    Course,
    Enrollment,
    Teacher
)
from .serializers import (
    StudentSerializer,
    StudentSerializerV2,
    TeacherSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    ListStudentEnrollmentSerializer,
    ListStudentsEnrolledByCourseSerializer
)

def home(request):
    return render(request,'core/home.html')


class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf', 'email']
    
    def get_serializer_class(self):
        if self.request.version =='v2':
            return StudentSerializerV2
        else:
            return StudentSerializer


class TeachersViewSet(viewsets.ModelViewSet):
    """Showing all teachers"""
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['name']
    search_fields = ['name', 'cpf', 'email']


class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status = status.HTTP_201_CREATED)
            id = str(serializer.data['id'])
            response['Location'] = request.build_absolute_uri() + id
            return response


class EnrollmentViewSet(viewsets.ModelViewSet):
    """Showing all school enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    http_method_names = ['get', 'post', 'put', 'patch']
    
    @method_decorator(cache_page(30))
    def dispatch(self, *args, **kwargs):
        return super(EnrollmentViewSet, self).dispatch(*args, **kwargs)

class ListStudentEnrollment(generics.ListAPIView):
    """Listing the enrollments of a student"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentEnrollmentSerializer


class ListEnrolledStudents(generics.ListAPIView):
    """Listing enrolled students by course"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsEnrolledByCourseSerializer
