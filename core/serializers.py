from rest_framework import serializers
from .validators import *
from .models import (
    Student,
    Course,
    Enrollment
)


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'rg', 'cpf', 'date_of_birth', 'phonenumber', 'email']
        
    def validate(self, data):
        if not cpf_validator(data['cpf']):
            raise serializers.ValidationError(
                {
                    'cpf':'O CPF é inválido'
                })
        if not name_validator(data['name']):
            raise serializers.ValidationError(
                {
                'name':'O nome é inválido'
                })
        if not rg_validator(data['rg']):
            raise serializers.ValidationError(
                {
                'rg':'O RG é inválido'
                })
        if not phonenumber_validator(data['phonenumber']):
            raise serializers.ValidationError(
                {
                'phonenumber':'O nomero do celular deve seguir esse modelo: 11 91234-5678'
                })
        return data


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