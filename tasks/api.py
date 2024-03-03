from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from  rest_framework import status


# Esto genera todos los endpoints del crud de Task
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    # Esto permite añadir operaciones personalizadas
    # detail: Indica si va a ser aplicado para todas las instancias. True: Sólo para 1 instancia.
    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        task = self.get_object()
        task.done = not task.done
        task.save()

        return Response({'status': 'task marked as done' if task.done else 'task undone'}, status=status.HTTP_200_OK)




