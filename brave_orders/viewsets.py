"""Django REST Framework viewsets for the brave_orders application."""

import rest_framework.viewsets as viewsets  # pylint: disable=consider-using-from-import

import brave_orders.models as models  # pylint: disable=consider-using-from-import
import brave_orders.serializers as serializers  # pylint: disable=consider-using-from-import


class CustomerViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Customer CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /api/customers/ - List all customers
    - POST /api/customers/ - Create a new customer
    - GET /api/customers/{id}/ - Retrieve a specific customer
    - PUT /api/customers/{id}/ - Update a customer (full update)
    - PATCH /api/customers/{id}/ - Update a customer (partial update)
    - DELETE /api/customers/{id}/ - Delete a customer

    Attributes:
        queryset: The queryset of Customer objects to be used for the view.
            Returns all Customer instances.
        serializer_class: The serializer class to use for request/response
            serialization (CustomerSerializer).

    Example:
        The ViewSet automatically handles HTTP methods:
        - GET request to /api/customers/ returns a list of all customers
        - POST request to /api/customers/ creates a new customer
        - GET request to /api/customers/1/ returns the customer with id=1
    """

    queryset = models.Customer.objects.all()  # pylint: disable=no-member
    serializer_class = serializers.CustomerSerializer


class SellerViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Seller CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /api/sellers/ - List all sellers
    - POST /api/sellers/ - Create a new seller
    - GET /api/sellers/{id}/ - Retrieve a specific seller
    - PUT /api/sellers/{id}/ - Update a seller (full update)
    - PATCH /api/sellers/{id}/ - Update a seller (partial update)
    - DELETE /api/sellers/{id}/ - Delete a seller

    Attributes:
        queryset: The queryset of Seller objects to be used for the view.
            Returns all Seller instances.
        serializer_class: The serializer class to use for request/response
            serialization (SellerSerializer).

    Example:
        The ViewSet automatically handles HTTP methods:
        - GET request to /api/sellers/ returns a list of all sellers
        - POST request to /api/sellers/ creates a new seller
        - GET request to /api/sellers/1/ returns the seller with id=1
    """

    queryset = models.Seller.objects.all()  # pylint: disable=no-member
    serializer_class = serializers.SellerSerializer


class OrderViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Order CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /api/orders/ - List all orders
    - POST /api/orders/ - Create a new order
    - GET /api/orders/{id}/ - Retrieve a specific order
    - PUT /api/orders/{id}/ - Update an order (full update)
    - PATCH /api/orders/{id}/ - Update an order (partial update)
    - DELETE /api/orders/{id}/ - Delete an order

    Attributes:
        queryset: The queryset of Order objects to be used for the view.
            Returns all Order instances.
        serializer_class: The serializer class to use for request/response
            serialization (OrderSerializer).

    Example:
        The ViewSet automatically handles HTTP methods:
        - GET request to /api/orders/ returns a list of all orders
        - POST request to /api/orders/ creates a new order
        - GET request to /api/orders/1/ returns the order with id=1
    """

    queryset = models.Order.objects.all()  # pylint: disable=no-member
    serializer_class = serializers.OrderSerializer


class AdvertisementViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Advertisement CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /api/advertisements/ - List all advertisements
    - POST /api/advertisements/ - Create a new advertisement
    - GET /api/advertisements/{id}/ - Retrieve a specific advertisement
    - PUT /api/advertisements/{id}/ - Update an advertisement (full update)
    - PATCH /api/advertisements/{id}/ - Update an advertisement (partial update)
    - DELETE /api/advertisements/{id}/ - Delete an advertisement

    Attributes:
        queryset: The queryset of Advertisement objects to be used for the view.
            Returns all Advertisement instances.
        serializer_class: The serializer class to use for request/response
            serialization (AdvertisementSerializer).

    Example:
        The ViewSet automatically handles HTTP methods:
        - GET request to /api/advertisements/ returns a list of all advertisements
        - POST request to /api/advertisements/ creates a new advertisement
        - GET request to /api/advertisements/1/ returns the advertisement with id=1
    """

    queryset = models.Advertisement.objects.all()  # pylint: disable=no-member
    serializer_class = serializers.AdvertisementSerializer


class AdvertisementKindViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling AdvertisementKind CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /api/advertisement-kinds/ - List all advertisement kinds
    - POST /api/advertisement-kinds/ - Create a new advertisement kind
    - GET /api/advertisement-kinds/{id}/ - Retrieve a specific advertisement kind
    - PUT /api/advertisement-kinds/{id}/ - Update an advertisement kind (full update)
    - PATCH /api/advertisement-kinds/{id}/ - Update an advertisement kind (partial update)
    - DELETE /api/advertisement-kinds/{id}/ - Delete an advertisement kind

    Attributes:
        queryset: The queryset of AdvertisementKind objects to be used for the view.
            Returns all AdvertisementKind instances.
        serializer_class: The serializer class to use for request/response
            serialization (AdvertisementKindSerializer).

    Example:
        The ViewSet automatically handles HTTP methods:
        - GET request to /api/advertisement-kinds/ returns a list of all kinds
        - POST request to /api/advertisement-kinds/ creates a new kind
        - GET request to /api/advertisement-kinds/1/ returns the kind with id=1
    """

    queryset = (
        models.AdvertisementKind.objects.all()
    )  # pylint: disable=no-member
    serializer_class = serializers.AdvertisementKindSerializer


class AdvertisementElementViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling AdvertisementElement CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /api/advertisement-elements/ - List all advertisement elements
    - POST /api/advertisement-elements/ - Create a new advertisement element
    - GET /api/advertisement-elements/{id}/ - Retrieve a specific advertisement element
    - PUT /api/advertisement-elements/{id}/ - Update an advertisement element (full update)
    - PATCH /api/advertisement-elements/{id}/ - Update an advertisement element (partial update)
    - DELETE /api/advertisement-elements/{id}/ - Delete an advertisement element

    Attributes:
        queryset: The queryset of AdvertisementElement objects to be used for the view.
            Returns all AdvertisementElement instances.
        serializer_class: The serializer class to use for request/response
            serialization (AdvertisementElementSerializer).

    Example:
        The ViewSet automatically handles HTTP methods:
        - GET request to /api/advertisement-elements/ returns a list of all elements
        - POST request to /api/advertisement-elements/ creates a new element
        - GET request to /api/advertisement-elements/1/ returns the element with id=1
    """

    queryset = (
        models.AdvertisementElement.objects.all()
    )  # pylint: disable=no-member
    serializer_class = serializers.AdvertisementElementSerializer
