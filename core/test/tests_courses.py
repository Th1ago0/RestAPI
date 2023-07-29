from rest_framework.test import APITestCase
from core.models import Course
from django.urls import reverse
from rest_framework import status

class CourseTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Courses-list')
        self.course_1 = Course.objects.create(
            course_code = 'POO',
            description = 'Programação orientada a objetos',
            level = 'I'
            )
        self.course_2 = Course.objects.create(
            course_code = 'TSCPT',
            description = 'Typescript',
            level = 'A'
            )
    
    def test_request_get(self):
        """Test to verify the GET method to list courses"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_request_post(self):
        data = {
            'course_code':'IT',
            'description':'Tecnology',
            'level':'B'
        }
        response = self.client.post(self.list_url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    #def testing(self):
    #    self.fail('teste falhador')