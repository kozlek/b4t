from rest_framework import viewsets

from .nosql_models import EventModel
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = EventModel.objects.all()
    serializer_class = EventSerializer
