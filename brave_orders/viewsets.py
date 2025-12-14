"""Django REST Framework viewsets and serializers for the brave_orders application."""

from rest_framework import serializers, viewsets

from . import models


class CustomerSerializer(
    serializers.ModelSerializer
):  # pylint: disable=too-few-public-methods
    """Serializer for the Customer model.

    This serializer handles serialization and deserialization of Customer instances
    for API requests and responses. It includes all fields from the Customer model
    and provides validation for the data.

    Attributes:
        Meta.model: The Django model class to serialize (Customer).
        Meta.fields: Specifies that all model fields should be included in the
            serialization.

    Example:
        >>> serializer = CustomerSerializer(data={
        ...     'name': 'Acme Corp',
        ...     'ruc': '12345678901',
        ...     'email': 'contact@acme.com',
        ...     'phone': '+1234567890',
        ...     'address': '123 Main St',
        ...     'contact_name': 'John Doe'
        ... })
        >>> serializer.is_valid()
        True
        >>> customer = serializer.save()
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta configuration for CustomerSerializer."""

        model = models.Customer
        fields = "__all__"


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
    serializer_class = CustomerSerializer
