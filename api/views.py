from django.db.models import Q
from rest_framework import viewsets

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a note instance.

        list:
            Return all notes, ordered by id.

        create:
            Create a new note.

        delete:
            Remove an existing note.

        partial_update:
            Update one or more fields on an existing user.

        update:
            Update a user.
    """
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        query = self.request.query_params.get('query')
        queryset = Task.objects.filter(Q(title__contains=query) | Q(content__contains=query)).order_by(
            'id')

        return queryset
