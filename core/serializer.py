from rest_framework import serializers
from .models import (
    Student,
    Course,
    Enrollment
)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'date_of_birth']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = []


class ListStudentEnrollmentSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source = 'course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Enrollment
        fields = ['course', 'period']
    def get_period(self, obj):
        return obj.get_period_display()


class ListStudentsEnrolledByCourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source = 'student.name')
    class Meta:
        model = Enrollment
        fields = ['student_name']