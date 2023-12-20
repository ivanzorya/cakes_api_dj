from django.urls import include, path
from rest_framework import routers

from api.views.cakes import CakesModelViewSet

router = routers.DefaultRouter()
router.register(r"cakes", CakesModelViewSet, basename="cakes")


urlpatterns = [
    path("", include(router.urls)),
]
