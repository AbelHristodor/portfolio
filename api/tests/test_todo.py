from django.test import TestCase
from api.tests import UserFactory, TodoItemFactory
import json


class TodoTestTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory(is_superuser=True)
        self.todo_item = TodoItemFactory()

    def test_list_todos(self):
        """Test that an authenticated user cam list all todos"""
        self.client.force_login(user=self.user)
        response = self.client.get(
            "/api/todo/getAll/",
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(
                response.status_code,
                200
        )
        response_json = response.json()
        self.assertEqual(response_json[0]['pk'], self.todo_item.id)
        self.assertEqual(response_json[0]['fields']['text'], self.todo_item.text)

    def test_add_todo(self):
        """Test that an authenticated user can add a new todo"""
        self.client.force_login(user=self.user)
        response = self.client.post(
            "/api/todo/add/",
            {
                "text": "testing"
            }
        )
        self.assertEqual(
            response.status_code,
            200
        )

    def test_delete_todo(self):
        """Test that an authenticated user can delete a todo"""
        self.client.force_login(user=self.user)
        response = self.client.post(
            "/api/todo/delete/",
            {
                "id": self.todo_item.id
            }
        )

        self.assertEqual(
            response.status_code,
            200
        )

    def test_not_authenticated_list_todo(self):
        """Test that a not authenticated user cannot list all todos"""
        response = self.client.get(
            "/api/todo/getAll/",
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(
            response.status_code,
            302
        )

    def test_not_authenticated_add_todo(self):
        """Test that a not authenticated user cannot add a new todo"""
        response = self.client.post(
            "/api/todo/add/",
            {
                "text": "testing"
            }
        )
        self.assertEqual(
            response.status_code,
            302
        )

    def test_not_authenticated_delete_todo(self):
        """Test that a not authenticated user cannot delete a todo"""
        response = self.client.post(
            "/api/todo/delete/",
            {
                "id": self.todo_item.id
            }
        )

        self.assertEqual(
            response.status_code,
            302
        )


