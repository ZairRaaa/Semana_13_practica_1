from rest_framework.viewsets import ModelViewSet

from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    filterset_fields = ["estado"]
    search_fields = ["titulo"]
    ordering_fields = ["id", "titulo", "fecha_inicio", "fecha_limite"]
