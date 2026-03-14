from django.views.generic import ListView
from app.models import Todo

class TodoListView(ListView):
    model = Todo
    template_name = 'app/list.html'
    context_object_name = 'tasks'
    ordering = ['-created_at']
    paginate_by = 20
