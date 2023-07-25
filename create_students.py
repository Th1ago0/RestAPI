import os
import django 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.utils import timezone
from faker import Faker
from validate_docbr import CPF
from core.models import Student
import random

def create_person(amount_of_people):
    """This function creates random students and puts them in the db"""
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(amount_of_people):
        cpf = CPF()
        cpf = cpf.generate()
        name = fake.name()
        email = '{}@{}'.format(name.lower(), fake.free_email_domain())
        email = email.replace(' ', '')
        rg = '{}{}{}{}'.format(random.randrange(10, 99), random.randrange(100, 999), random.randrange(100, 999), random.randrange(100, 999), random.randrange(0, 9))
        phonenumber = '{} 9{}-{}'.format(random.randrange(10, 21), random.randrange(4000, 9999), random.randrange(4000, 9999))
        date_of_birth = timezone.now()

        student = Student(name = name, cpf = cpf,  email = email, date_of_birth = date_of_birth, rg = rg, phonenumber = phonenumber)
        student.save()

create_person(50)
print('success')