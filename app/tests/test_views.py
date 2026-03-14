from django.test import TestCase
from django.urls import reverse
from app.models import Todo

class TaskListViewTest(TestCase):
    def setUp(self):
        # Create some mock tasks
        Todo.objects.create(title="Task 1", completed=False)
        Todo.objects.create(title="Task 2", completed=True)

    def test_list_view_status_code(self):
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, 200)

    def test_list_view_template(self):
        response = self.client.get(reverse('task-list'))
        self.assertTemplateUsed(response, 'app/list.html')

    def test_list_view_context(self):
        response = self.client.get(reverse('task-list'))
        self.assertTrue('tasks' in response.context)
        self.assertEqual(len(response.context['tasks']), 2)

    def test_list_view_ordering(self):
        # Add a third task to verify ordering (newest first)
        Todo.objects.create(title="Task 3")
        response = self.client.get(reverse('task-list'))
        tasks = response.context['tasks']
        self.assertEqual(tasks[0].title, "Task 3")
