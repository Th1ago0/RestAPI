from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import (
    Student,
    Course,
    Enrollment
)
from .serializer import (
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    ListStudentEnrollmentSerializer,
    ListStudentsEnrolledByCourseSerializer
)

class StudentsViewSet(viewsets.ModelViewSet):
    """Showing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    """Showing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EnrollmentViewSet(viewsets.ModelViewSet):
    """Showing all school enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListStudentEnrollment(generics.ListAPIView):
    """Listing the enrollments of a student"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentEnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListEnrolledStudents(generics.ListAPIView):
    """Listing enrolled students by course"""
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListStudentsEnrolledByCourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]