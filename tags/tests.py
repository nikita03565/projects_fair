from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from .models import Tag
from .serializers import TagSerializer

import json


class TagsTests(APITestCase):
    def setUp(self):
        self.url = reverse("tag-list")
        self.user_data = {'email': 'foobar@example.com', 'password': 'somepassword'}
        data = {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
            'first_name': 'First',
            'last_name': 'Last'
        }
        self.client.post(reverse("signup"), data, format='json')
        self.tag = [Tag.objects.create(name="tag1"),
                    Tag.objects.create(name="tag2"),
                    Tag.objects.create(name="tag3")
                    ]

    def test_get_tags(self):
        response = self.client.get(reverse("tag-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        tag_serializer_data = json.dumps(TagSerializer(instance=self.tag, many=True).data)
        tag_serializer_data = json.loads(tag_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(tag_serializer_data, response_data)

    def test_get_tag(self):
        response = self.client.get(reverse("tag-detail", kwargs={"pk": 2}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        tag_serializer_data = json.dumps(TagSerializer(instance=self.tag[1], many=False).data)
        tag_serializer_data = json.loads(tag_serializer_data)
        response_data = json.loads(response.content)
        self.assertEqual(tag_serializer_data, response_data)

    def test_post_tag_unauthorized(self):
        response = self.client.post(reverse("tag-list"), data={"name": "new_tag"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_post_tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.post(reverse("tag-list"), data={"name": "new_tag"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'new_tag')

    def test_put_tag_unauthorized(self):
        response = self.client.put(reverse("tag-detail", kwargs={"pk": 2}), data={"name": "new_tag"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_put_tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.put(reverse("tag-detail", kwargs={"pk": 2}), data={"name": "new_tag"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_tag')

    def test_patch_tag_unauthorized(self):
        response = self.client.patch(reverse("tag-detail", kwargs={"pk": 3}), data={"name": "new_tag"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.patch(reverse("tag-detail", kwargs={"pk": 3}), data={"name": "new_tag"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'new_tag')

    def test_delete_tag_unauthorized(self):
        response = self.client.delete(reverse("tag-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_tag_authorized(self):
        response = self.client.post(reverse("signin"), self.user_data, format='json')
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + response.data['token'])
        response = client.delete(reverse("tag-detail", kwargs={"pk": 3}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
