from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 64)
    rg = models.CharField(max_length = 9)
    cpf = models.CharField(max_length = 11)
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado')
    )
    
    course_code = models.CharField(max_length = 10)
    description = models.CharField(max_length = 64)
    level = models.CharField(max_length = 1, choices = LEVEL, blank = False, null = False, default = 'B' )
    
    def __str__(self):
        return self.description


class Enrollment(models.Model):
    PERIOD = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno')
    )
    
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    period = models.CharField(max_length = 1, choices = PERIOD, blank = False, null = False, default = 'M')
