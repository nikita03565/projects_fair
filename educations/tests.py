from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from .models import University, EduProgram, Faculty
from .serializers import UniversitySerializer, EduProgramSerializer, FacultySerializer

import json


class UniversitiesTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url_list = "university-list"
        cls.url_detail = "university-detail"
        cls.serializer = UniversitySerializer
        cls.Universities = [University.objects.create(name="University1"),
                            University.objects.create(name="University2"),
                            University.objects.create(name="University3")
                            ]
        cls.user_data = {'email': 'foobar@example.com', 'password': 'somepassword'}
        cls.data = {
            'email': cls.user_data['email'],
            'password': cls.user_data['password'],
            'first_name': 'First',
            'last_name': 'Last'
        }
        cls.client = APIClient()
        cls.client.post(reverse("signup"), cls.data, format='json')

    def test_get_Universities(self):
        response = self.client.get(reverse(self.url_list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.Universities, many=True).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_get_University(self):
        response = self.client.get(reverse(self.url_detail, kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.Universities[1], many=False).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_post_University_unauthorized(self):
        response = self.client.post(reverse(self.url_list), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.post(reverse(self.url_list), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_University')

    def test_put_University_unauthorized(self):
        response = self.client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_University')

    def test_patch_University_unauthorized(self):
        response = self.client.patch(reverse(self.url_detail, kwargs={"pk": 3}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.patch(reverse(self.url_detail, kwargs={"pk": 3}), data={"name": "new_University"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_University')

    def test_delete_University_unauthorized(self):
        response = self.client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_University_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class EduProgramsTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url_list = "eduprogram-list"
        cls.url_detail = "eduprogram-detail"
        cls.serializer = EduProgramSerializer
        cls.EduPrograms = [EduProgram.objects.create(name="EduProgram1"),
                           EduProgram.objects.create(name="EduProgram2"),
                           EduProgram.objects.create(name="EduProgram3")
                           ]
        cls.user_data = {'email': 'foobar@example.com', 'password': 'somepassword'}
        cls.data = {
            'email': cls.user_data['email'],
            'password': cls.user_data['password'],
            'first_name': 'First',
            'last_name': 'Last'
        }
        cls.client = APIClient()
        cls.client.post(reverse("signup"), cls.data, format='json')

    def test_get_EduPrograms(self):
        response = self.client.get(reverse(self.url_list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.EduPrograms, many=True).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_get_EduProgram(self):
        response = self.client.get(reverse(self.url_detail, kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.EduPrograms[1], many=False).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_post_EduProgram_unauthorized(self):
        response = self.client.post(reverse(self.url_list), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.post(reverse(self.url_list), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_EduProgram')

    def test_put_EduProgram_unauthorized(self):
        response = self.client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_EduProgram')

    def test_patch_EduProgram_unauthorized(self):
        response = self.client.patch(reverse(self.url_detail, kwargs={"pk": 3}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.patch(reverse(self.url_detail, kwargs={"pk": 3}), data={"name": "new_EduProgram"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_EduProgram')

    def test_delete_EduProgram_unauthorized(self):
        response = self.client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_EduProgram_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class FacultiesTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url_list = "faculty-list"
        cls.url_detail = "faculty-detail"
        cls.serializer = FacultySerializer
        cls.Faculties = [Faculty.objects.create(name="Faculty1"),
                         Faculty.objects.create(name="Faculty2"),
                         Faculty.objects.create(name="Faculty3")
                         ]
        cls.user_data = {'email': 'foobar@example.com', 'password': 'somepassword'}
        cls.data = {
            'email': cls.user_data['email'],
            'password': cls.user_data['password'],
            'first_name': 'First',
            'last_name': 'Last'
        }
        cls.client = APIClient()
        cls.client.post(reverse("signup"), cls.data, format='json')

    def test_get_Faculties(self):
        response = self.client.get(reverse(self.url_list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.Faculties, many=True).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_get_Faculty(self):
        response = self.client.get(reverse(self.url_detail, kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.Faculties[1], many=False).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_post_Faculty_unauthorized(self):
        response = self.client.post(reverse(self.url_list), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.post(reverse(self.url_list), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_Faculty')

    def test_put_Faculty_unauthorized(self):
        response = self.client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_Faculty')

    def test_patch_Faculty_unauthorized(self):
        response = self.client.patch(reverse("university-detail", kwargs={"pk": 3}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.patch(reverse(self.url_detail, kwargs={"pk": 3}), data={"name": "new_Faculty"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_Faculty')

    def test_delete_Faculty_unauthorized(self):
        response = self.client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_Faculty_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
