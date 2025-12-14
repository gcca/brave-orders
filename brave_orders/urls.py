"""URL configuration for the brave_orders application.

This module defines the URL routing for the brave_orders Django app, specifically
setting up REST API endpoints using Django REST Framework's DefaultRouter.

The router is configured to expose Customer resources at the /api/customers/ endpoint,
providing standard CRUD operations through the CustomerViewSet.
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = "brave-orders"  # pylint: disable=invalid-name

router = DefaultRouter()
router.register(r"customers", viewsets.CustomerViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]
