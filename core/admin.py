from django.contrib import admin
from .models import Student, Course, Enrollment

class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'date_of_birth', 'phonenumber', 'email')
    list_display_link = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20
    ordering = ('name',)


admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'course_code', 'description')
    list_display_link = ('id', 'course_code')
    search_fields = ('course_code',)


admin.site.register(Course, Courses)


class Enrollments(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'period')
    list_display_link = ('id',)


admin.site.register(Enrollment, Enrollments)