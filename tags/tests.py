from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from .models import Tag
from .serializers import TagSerializer

import json


class TagsTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.url_list = "tag-list"
        cls.url_detail = "tag-detail"
        cls.serializer = TagSerializer
        cls.Tags = [Tag.objects.create(name="Tag1"),
                    Tag.objects.create(name="Tag2"),
                    Tag.objects.create(name="Tag3")
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

    def test_get_Tags(self):
        response = self.client.get(reverse(self.url_list))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.Tags, many=True).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_get_Tag(self):
        response = self.client.get(reverse(self.url_detail, kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serializer_data = json.dumps(self.serializer(instance=self.Tags[1], many=False).data)
        serializer_data = json.loads(serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_post_Tag_unauthorized(self):
        response = self.client.post(reverse(self.url_list), data={"name": "new_Tag"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_Tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.post(reverse(self.url_list), data={"name": "new_Tag"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_Tag')

    def test_put_Tag_unauthorized(self):
        response = self.client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_Tag"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_Tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.put(reverse(self.url_detail, kwargs={"pk": 2}), data={"name": "new_Tag"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_Tag')

    def test_patch_Tag_unauthorized(self):
        response = self.client.patch(reverse(self.url_detail, kwargs={"pk": 3}), data={"name": "new_Tag"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_Tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.patch(reverse(self.url_detail, kwargs={"pk": 3}), data={"name": "new_Tag"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_Tag')

    def test_delete_Tag_unauthorized(self):
        response = self.client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_Tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = self.client.delete(reverse(self.url_detail, kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

