from datetime import date

from django.utils import timezone

from django.test import TestCase
from django.urls import reverse

from todo_list.models import Task


class TaskTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="test",
            datetime=timezone.now(),
            deadline=date(2026, 6, 10),
            done=False,
        )

    def test_task_creation(self):

        url = reverse("todo_list:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.task.content)

        self.assertContains(response, "False")
