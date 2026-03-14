from django.test import TestCase
from app.models import Todo

class TodoModelTest(TestCase):
    def test_todo_creation(self):
        """Test that a todo item can be created with a title and default values."""
        todo = Todo.objects.create(title="Test Task", description="This is a test description")
        self.assertEqual(todo.title, "Test Task")
        self.assertEqual(todo.description, "This is a test description")
        self.assertFalse(todo.completed)
        self.assertIsNotNone(todo.created_at)

    def test_mark_as_completed(self):
        """Test that a todo item can be marked as completed."""
        todo = Todo.objects.create(title="Incomplete Task")
        todo.completed = True
        todo.save()
        
        updated_todo = Todo.objects.get(id=todo.id)
        self.assertTrue(updated_todo.completed)

    def test_str_representation(self):
        """Test the string representation of the Todo model."""
        todo = Todo.objects.create(title="My String Test")
        self.assertEqual(str(todo), "My String Test")
