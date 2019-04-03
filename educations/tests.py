from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from .models import University, EduProgram, Faculty
from .serializers import UniversitySerializer

import json


class UniversitiesTests(APITestCase):
    def setUp(self):
        self.url = reverse("university-list")
        self.user_data = {'email': 'foobar@example.com', 'password': 'somepassword'}
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
            'first_name': 'First',
            'last_name': 'Last'
        }
        self.client.post(reverse("signup"), data, format='json')
        self.Universities = [University.objects.create(name="University1"),
                             University.objects.create(name="University2"),
                             University.objects.create(name="University3")
                             ]

    def test_get_Universities(self):
        response = self.client.get(reverse("university-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        university_serializer_data = json.dumps(UniversitySerializer(instance=self.Universities, many=True).data)
        university_serializer_data = json.loads(university_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(university_serializer_data, response_data)

    def test_get_University(self):
        response = self.client.get(reverse("university-detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        university_serializer_data = json.dumps(UniversitySerializer(instance=self.Universities[1], many=False).data)
        university_serializer_data = json.loads(university_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(university_serializer_data, response_data)

    def test_post_University_unauthorized(self):
        response = self.client.post(reverse("university-list"), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.post(reverse("university-list"), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_University')

    def test_put_University_unauthorized(self):
        response = self.client.put(reverse("university-detail", kwargs={"pk": 2}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.put(reverse("university-detail", kwargs={"pk": 2}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_University')

    def test_patch_University_unauthorized(self):
        response = self.client.patch(reverse("university-detail", kwargs={"pk": 3}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.patch(reverse("university-detail", kwargs={"pk": 3}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_University')

    def test_delete_University_unauthorized(self):
        response = self.client.delete(reverse("university-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.delete(reverse("university-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class EduProgramsTests(APITestCase):
    def setUp(self):
        self.url = reverse("eduprogram-list")
        self.user_data = {'email': 'foobar@example.com', 'password': 'somepassword'}
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
            'first_name': 'First',
            'last_name': 'Last'
        }
        self.client.post(reverse("signup"), data, format='json')
        self.EduPrograms = [EduProgram.objects.create(name="EduProgram1"),
                            EduProgram.objects.create(name="EduProgram2"),
                            EduProgram.objects.create(name="EduProgram3")
                            ]

    def test_get_EduPrograms(self):
        response = self.client.get(reverse("eduprogram-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        university_serializer_data = json.dumps(UniversitySerializer(instance=self.EduPrograms, many=True).data)
        university_serializer_data = json.loads(university_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(university_serializer_data, response_data)

    def test_get_EduProgram(self):
        response = self.client.get(reverse("eduprogram-detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        university_serializer_data = json.dumps(UniversitySerializer(instance=self.EduPrograms[1], many=False).data)
        university_serializer_data = json.loads(university_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(university_serializer_data, response_data)

    def test_post_EduProgram_unauthorized(self):
        response = self.client.post(reverse("eduprogram-list"), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.post(reverse("university-list"), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_EduProgram')

    def test_put_EduProgram_unauthorized(self):
        response = self.client.put(reverse("eduprogram-detail", kwargs={"pk": 2}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.put(reverse("eduprogram-detail", kwargs={"pk": 2}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_EduProgram')

    def test_patch_EduProgram_unauthorized(self):
        response = self.client.patch(reverse("university-detail", kwargs={"pk": 3}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.patch(reverse("eduprogram-detail", kwargs={"pk": 3}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_EduProgram')

    def test_delete_EduProgram_unauthorized(self):
        response = self.client.delete(reverse("eduprogram-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.delete(reverse("eduprogram-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FacultiesTests(APITestCase):
    def setUp(self):
        self.url = reverse("faculty-list")
        self.user_data = {'email': 'foobar@example.com', 'password': 'somepassword'}
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
            'first_name': 'First',
            'last_name': 'Last'
        }
        self.client.post(reverse("signup"), data, format='json')
        self.Faculties = [Faculty.objects.create(name="Faculty1"),
                          Faculty.objects.create(name="Faculty2"),
                          Faculty.objects.create(name="Faculty3")
                          ]

    def test_get_Faculties(self):
        response = self.client.get(reverse("faculty-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        university_serializer_data = json.dumps(UniversitySerializer(instance=self.Faculties, many=True).data)
        university_serializer_data = json.loads(university_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(university_serializer_data, response_data)

    def test_get_Faculty(self):
        response = self.client.get(reverse("faculty-detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        university_serializer_data = json.dumps(UniversitySerializer(instance=self.Faculties[1], many=False).data)
        university_serializer_data = json.loads(university_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(university_serializer_data, response_data)

    def test_post_Faculty_unauthorized(self):
        response = self.client.post(reverse("faculty-list"), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.post(reverse("university-list"), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_Faculty')

    def test_put_Faculty_unauthorized(self):
        response = self.client.put(reverse("faculty-detail", kwargs={"pk": 2}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.put(reverse("faculty-detail", kwargs={"pk": 2}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_Faculty')

    def test_patch_Faculty_unauthorized(self):
        response = self.client.patch(reverse("university-detail", kwargs={"pk": 3}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.patch(reverse("faculty-detail", kwargs={"pk": 3}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_Faculty')

    def test_delete_Faculty_unauthorized(self):
        response = self.client.delete(reverse("faculty-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.delete(reverse("faculty-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
