from rest_framework.test import APITestCase
from rest_framework import status
from .models import User
from rest_framework.authtoken.models import Token


class AccountTests(APITestCase):
    def test_new_user_registration(self):
        url = "http://127.0.0.1:8000/api/v1/reg"
        data = {
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['email'], data['email'])
        self.assertFalse('password' in response.data)
        token = Token.objects.get(user=User.objects.latest('id'))
        self.assertEqual(response.data['token'], token.key)

    def test_registration_user_with_short_password(self):
        url = "http://127.0.0.1:8000/api/v1/reg"
        data = {

            'email': 'foobarbaz@example.com',
            'password': 'foo',
            'first_name': 'First',
            'last_name': 'Last'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(len(response.data['password']), 1)

    def test_registration_user_with_no_password(self):
        url = "http://127.0.0.1:8000/api/v1/reg"
        data = {
            'email': 'foobarbaz@example.com',
            'password': '',
            'first_name': 'First',
            'last_name': 'Last'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(len(response.data['password']), 1)

    def test_create_user_with_invalid_email(self):
        url = "http://127.0.0.1:8000/api/v1/reg"
        data = {
            'email': 'testing',
            'passsword': 'foobarbaz',
            'first_name': 'First',
            'last_name': 'Last'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(len(response.data['email']), 1)

    def test_registration_user_with_no_email(self):
        url = "http://127.0.0.1:8000/api/v1/reg"
        data = {
            'email': '',
            'password': 'foobar123',
            'first_name': 'First',
            'last_name': 'Last'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(len(response.data['email']), 1)

    def test_registration_user_with_preexisting_email(self):

        url = "http://127.0.0.1:8000/api/v1/reg"
        data = {
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last'
        }
        User.objects.create_user_by_email(data["email"], data["password"], data["first_name"], data["last_name"])
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_authorize_registered_user(self):
        url = "http://127.0.0.1:8000/api/v1/reg"
        data = {
            'email': 'foobar@example.com',
            'password': 'somepassword',
            'first_name': 'First',
            'last_name': 'Last'
        }
        response = self.client.post(url, data, format='json')
        token1 = response.data['token']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        url = "http://127.0.0.1:8000/api/v1/auth"
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(token1, response.data['token'])

    def test_authorize_user(self):
        self.user = User.objects.create_user(username='testUser', password='12345', email="test@test.test")
        url = "http://127.0.0.1:8000/api/v1/auth"
        data = {'email': 'test@test.test', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authorize_empty_fields(self):
        url = "http://127.0.0.1:8000/api/v1/auth"
        data = {'email': '', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['email'][0], "This field may not be blank.")
        
        data = {'email': 'test@test.test', 'password': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], "This field may not be blank.")

        data = {'email': '', 'password': ''}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['password'][0], "This field may not be blank.")
        self.assertEqual(response.data['email'][0], "This field may not be blank.")

    def test_authorize_wrongData(self):
        url = "http://127.0.0.1:8000/api/v1/auth"
        data = {'email': 'wrongtest@test.tes', 'password': '12345'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        data = {'email': 'test@test.test', 'password': '12345wrong7'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_change_password_no_authorized(self):
        url = "http://127.0.0.1:8000/api/v1/chpass"
        self.user = User.objects.create_user(username='testUser', password='12345', email="test@test.test")
        response = self.client.post(url, {'new_password': "12345678"}, format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)


