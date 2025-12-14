"""URL configuration for the brave_orders application.

This module defines the URL routing for the brave_orders Django app, specifically
setting up REST API endpoints using Django REST Framework's DefaultRouter.

The router is configured to expose the following resources:
- Customer resources at /api/customers/
- Seller resources at /api/sellers/
- Order resources at /api/orders/
- Advertisement resources at /api/advertisements/
- AdvertisementKind resources at /api/advertisement-kinds/
- AdvertisementElement resources at /api/advertisement-elements/

All endpoints provide standard CRUD operations through their respective ViewSets.
"""

import django.urls  # pylint: disable=consider-using-from-import
import rest_framework.routers  # pylint: disable=consider-using-from-import

import brave_orders.viewsets as viewsets  # pylint: disable=consider-using-from-import

app_name = "brave-orders"  # pylint: disable=invalid-name

router = rest_framework.routers.DefaultRouter()
router.register(r"customers", viewsets.CustomerViewSet)
router.register(r"sellers", viewsets.SellerViewSet)
router.register(r"orders", viewsets.OrderViewSet)
router.register(r"advertisements", viewsets.AdvertisementViewSet)
router.register(r"advertisement-kinds", viewsets.AdvertisementKindViewSet)
router.register(r"advertisement-elements", viewsets.AdvertisementElementViewSet)

urlpatterns = [
    django.urls.path("api/", django.urls.include(router.urls)),
]
