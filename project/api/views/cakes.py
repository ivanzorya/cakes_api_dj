from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.serializers import CakeSerializer
from cakes.models import Cake


class CakesModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Cake.objects.all()
    serializer_class = CakeSerializer
    permission_classes = (AllowAny,)
