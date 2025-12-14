"""URL configuration for the brave_orders application.

This module defines the URL routing for the brave_orders Django app, specifically
setting up REST API endpoints using Django REST Framework's DefaultRouter.

The router is configured to expose Customer resources at the /api/customers/ endpoint,
providing standard CRUD operations through the CustomerViewSet.
"""

import django.urls  # pylint: disable=consider-using-from-import
import rest_framework.routers  # pylint: disable=consider-using-from-import

import brave_orders.viewsets as viewsets  # pylint: disable=consider-using-from-import

app_name = "brave-orders"  # pylint: disable=invalid-name

router = rest_framework.routers.DefaultRouter()
router.register(r"customers", viewsets.CustomerViewSet)

urlpatterns = [
    django.urls.path("api/", django.urls.include(router.urls)),
]
