from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from rest_framework.test import APIClient
# Create your tests here.


class AuthorizationTests(APITestCase):
    def test_authorizeUser(self):
        self.user = User.objects.create_user(username='testUser', password='12345',email="test@test.test")
        url = "http://127.0.0.1:8000/api/v1/auth"
        data = {'email': 'test@test.test', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_emptyFields(self):
        url = "http://127.0.0.1:8000/api/v1/auth"
        data = {'email': '', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0],"This field may not be blank.")
        
        data = {'email': 'test@test.test', 'password': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], "This field may not be blank.")

        data = {'email': '', 'password': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], "This field may not be blank.")
        self.assertEqual(response.data['email'][0], "This field may not be blank.")

    def test_wrongData(self):
        url = "http://127.0.0.1:8000/api/v1/auth"
        data = {'email': 'wrongtest@test.test', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)

        data = {'email': 'test@test.test', 'password': '12345wrong7'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
