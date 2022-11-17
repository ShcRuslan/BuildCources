from django.test import TestCase
from django.urls import reverse, resolve

from rest_framework import status
from mycource.models import Category, Course
from mycource.serializers import CourseSerializer
from mycource.views import CourseList, CourseDetail


class AuthorTestViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_courses = 5
        for course in range(number_of_courses):
            cat = Category.objects.create(name='Programming', imgpath='programmingPicture')
            Course.objects.create(name='Neobis', description='bla bla bla', category=cat, logo='some logo')

    def course_list_test(self):
        resp = self.client.get(reverse('courses_list'))
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        
        self.assertEqual(resp.data, serializer.data)

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def course_post_test(self):
        example = {
        "id": 1,
        "name": "Neolabs",
        "description": "Very good course",
        "category": {
            "id": 1,
            "name": "programming",
            "imgpath": "45456"
        },
        "logo": "NeoLabs",
        "contacts": [
            {
                "id": 1,
                "type": 1,
                "value": "45456"
            }
        ],
        "branches": [
            {
                "id": 1,
                "latitude": "5674",
                "longitude": "5678",
                "address": "Tinistanov st."
            }
        ]
        }

        resp = self.client.get(reverse('courses_list'), example, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)



    def test_course_list_examination(self):
        url = reverse('courses_list')
        self.assertEquals(resolve(url).func.view_class, CourseList)