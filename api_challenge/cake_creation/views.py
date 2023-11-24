from cake_creation.serializers import CakeSerializer
from cake_creation.models import Cake
from rest_framework.mixins import (
    ListModelMixin,CreateModelMixin, DestroyModelMixin)
from rest_framework.viewsets import GenericViewSet

class CakeView(ListModelMixin,CreateModelMixin,DestroyModelMixin,GenericViewSet):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
    ordering_fields = "__all__"