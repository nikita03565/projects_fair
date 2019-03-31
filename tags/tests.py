from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from .models import Tag
from .serializers import TagSerializer
from users.models import User
import json


class TagsTests(APITestCase):
    def setUp(self):
        self.url = reverse("tag-list")
        self.user = User.objects.create_user_by_email(
            email='foobar@example.com',
            password='somepassword',
            first_name='First',
            last_name='Last'
        )
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
