from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = "brave-orders"

router = DefaultRouter()
router.register(r"customers", viewsets.CustomerViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
