from django.test import TestCase
from django.urls import reverse

from todo_list.models import Tag


class TagTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="test"
        )

    def test_create_tag(self):

        url = reverse("todo_list:tag-list")
        response = self.client.get(url)

        self.assertContains(response, self.tag.name)


        self.assertEqual(response.status_code, 200)


