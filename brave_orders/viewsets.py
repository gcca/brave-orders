"""Django REST Framework viewsets for the brave_orders application."""

import typing

import django.db.models.query as query  # pylint: disable=consider-using-from-import
import rest_framework.viewsets as viewsets  # pylint: disable=consider-using-from-import

import brave_orders.models as models  # pylint: disable=consider-using-from-import
import brave_orders.pagination as pagination  # pylint: disable=consider-using-from-import
import brave_orders.serializers as serializers  # pylint: disable=consider-using-from-import


class CustomerViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Customer CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /brave/orders/api/v1/customers/ - List all customers (paginated)
    - POST /brave/orders/api/v1/customers/ - Create a new customer
    - GET /brave/orders/api/v1/customers/{id}/ - Retrieve a specific customer
    - PUT /brave/orders/api/v1/customers/{id}/ - Update a customer (full update)
    - PATCH /brave/orders/api/v1/customers/{id}/ - Update a customer (partial update)
    - DELETE /brave/orders/api/v1/customers/{id}/ - Delete a customer

    Attributes:
        queryset: The queryset of Customer objects to be used for the view.
            Returns all Customer instances.
        serializer_class: The serializer class to use for request/response
            serialization (CustomerSerializer).

    Examples using httpie CLI:
        # List all customers (paginated, 50 per page)
        http GET http://localhost:8000/brave/orders/api/v1/customers/

        # Create a new customer
        echo '{"name":"Acme Corp","ruc":"12345678901",' \\
            '"email":"contact@acme.com","phone":"+1234567890",' \\
            '"address":"123 Main St","contact_name":"John Doe"}' | \\
            http POST http://localhost:8000/brave/orders/api/v1/customers/ \\
            Content-Type:application/json

        # Retrieve a specific customer
        http GET http://localhost:8000/brave/orders/api/v1/customers/1/

        # Update a customer (full update)
        echo '{"name":"Acme Corp Updated","ruc":"12345678901",' \\
            '"email":"newemail@acme.com","phone":"+1234567890",' \\
            '"address":"456 New St","contact_name":"Jane Doe"}' | \\
            http PUT http://localhost:8000/brave/orders/api/v1/customers/1/ \\
            Content-Type:application/json

        # Partial update a customer
        echo '{"email":"updated@acme.com"}' | \\
            http PATCH http://localhost:8000/brave/orders/api/v1/customers/1/ \\
            Content-Type:application/json

        # Delete a customer
        http DELETE http://localhost:8000/brave/orders/api/v1/customers/1/
    """

    queryset: query.QuerySet[models.Customer] = (
        models.Customer.objects.all()  # pylint: disable=no-member
    )
    serializer_class: typing.Type[serializers.CustomerSerializer] = (
        serializers.CustomerSerializer
    )
    pagination_class: typing.Type[pagination.StandardResultsSetPagination] = (
        pagination.StandardResultsSetPagination
    )


class SellerViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Seller CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /brave/orders/api/v1/sellers/ - List all sellers (paginated)
    - POST /brave/orders/api/v1/sellers/ - Create a new seller
    - GET /brave/orders/api/v1/sellers/{id}/ - Retrieve a specific seller
    - PUT /brave/orders/api/v1/sellers/{id}/ - Update a seller (full update)
    - PATCH /brave/orders/api/v1/sellers/{id}/ - Update a seller (partial update)
    - DELETE /brave/orders/api/v1/sellers/{id}/ - Delete a seller

    Attributes:
        queryset: The queryset of Seller objects to be used for the view.
            Returns all Seller instances.
        serializer_class: The serializer class to use for request/response
            serialization (SellerSerializer).

    Examples using httpie CLI:
        # List all sellers (paginated, 50 per page)
        http GET http://localhost:8000/brave/orders/api/v1/sellers/

        # Create a new seller
        echo '{"name":"Jane Smith","address":"456 Business Ave",' \\
            '"email":"jane@example.com","company_name":"Tech Solutions Inc",' \\
            '"ruc":"98765432109"}' | \\
            http POST http://localhost:8000/brave/orders/api/v1/sellers/ \\
            Content-Type:application/json

        # Retrieve a specific seller
        http GET http://localhost:8000/brave/orders/api/v1/sellers/1/

        # Update a seller (full update)
        echo '{"name":"Jane Smith Updated","address":"789 New Ave",' \\
            '"email":"jane.new@example.com","company_name":"New Tech Solutions",' \\
            '"ruc":"98765432109"}' | \\
            http PUT http://localhost:8000/brave/orders/api/v1/sellers/1/ \\
            Content-Type:application/json

        # Partial update a seller
        echo '{"email":"updated@example.com"}' | \\
            http PATCH http://localhost:8000/brave/orders/api/v1/sellers/1/ \\
            Content-Type:application/json

        # Delete a seller
        http DELETE http://localhost:8000/brave/orders/api/v1/sellers/1/
    """

    queryset: query.QuerySet[models.Seller] = (
        models.Seller.objects.all()  # pylint: disable=no-member
    )
    serializer_class: typing.Type[serializers.SellerSerializer] = (
        serializers.SellerSerializer
    )
    pagination_class: typing.Type[pagination.StandardResultsSetPagination] = (
        pagination.StandardResultsSetPagination
    )


class OrderViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Order CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /brave/orders/api/v1/orders/ - List all orders (paginated) with
        nested advertisements
    - POST /brave/orders/api/v1/orders/ - Create a new order with optional
        nested advertisements
    - GET /brave/orders/api/v1/orders/{id}/ - Retrieve a specific order with
        nested advertisements
    - PUT /brave/orders/api/v1/orders/{id}/ - Update an order (full update)
        with optional nested advertisements
    - PATCH /brave/orders/api/v1/orders/{id}/ - Update an order (partial update)
    - DELETE /brave/orders/api/v1/orders/{id}/ - Delete an order

    Attributes:
        queryset: The queryset of Order objects to be used for the view.
            Returns all Order instances.
        serializer_class: The serializer class to use for request/response
            serialization (OrderSerializer).

    Examples using httpie CLI:
        # List all orders (paginated, 50 per page, includes advertisements)
        http GET http://localhost:8000/brave/orders/api/v1/orders/

        # Create a new order with nested advertisements
        echo '{
          "customer": 1,
          "seller": 1,
          "ruc": "12345678901",
          "email": "order@example.com",
          "address": "123 Order St",
          "phone": "+1234567890",
          "contact_name": "Jane Doe",
          "payment_days": 30,
          "advertisements": [
            {
              "brand": "TechBrand",
              "code": "AD-2024-001",
              "start_date": "2024-01-01",
              "end_date": "2024-12-31",
              "quantity": 100,
              "unit_price": "50.00",
              "advertisement_element": 1,
              "advertisement_kind": 1
            }
          ]
        }' | http POST http://localhost:8000/brave/orders/api/v1/orders/ \\
            Content-Type:application/json

        # Create a new order without advertisements
        echo '{"customer":1,"seller":1,"ruc":"12345678901",' \\
            '"email":"order@example.com","address":"123 Order St",' \\
            '"phone":"+1234567890","contact_name":"Jane Doe",' \\
            '"payment_days":30}' | \\
            http POST http://localhost:8000/brave/orders/api/v1/orders/ \\
            Content-Type:application/json

        # Retrieve a specific order (includes advertisements list)
        http GET http://localhost:8000/brave/orders/api/v1/orders/1/

        # Update an order with nested advertisements (replaces all)
        echo '{
          "customer": 1,
          "seller": 1,
          "ruc": "12345678901",
          "email": "updated@example.com",
          "address": "456 New St",
          "phone": "+9876543210",
          "contact_name": "John Updated",
          "payment_days": 60,
          "advertisements": [
            {
              "brand": "NewBrand",
              "code": "AD-2024-002",
              "start_date": "2024-02-01",
              "end_date": "2024-12-31",
              "quantity": 150,
              "unit_price": "75.00",
              "advertisement_element": 1,
              "advertisement_kind": 1
            }
          ]
        }' | http PUT http://localhost:8000/brave/orders/api/v1/orders/1/ \\
            Content-Type:application/json

        # Partial update an order (does not affect advertisements)
        echo '{"payment_days":45}' | \\
            http PATCH http://localhost:8000/brave/orders/api/v1/orders/1/ \\
            Content-Type:application/json

        # Delete an order
        http DELETE http://localhost:8000/brave/orders/api/v1/orders/1/
    """

    queryset: query.QuerySet[models.Order] = (
        models.Order.objects.select_related(  # pylint: disable=no-member
            "customer", "seller"
        )
        .prefetch_related("advertisements")
        .all()
    )
    serializer_class: typing.Type[serializers.OrderSerializer] = (
        serializers.OrderSerializer
    )
    pagination_class: typing.Type[pagination.StandardResultsSetPagination] = (
        pagination.StandardResultsSetPagination
    )


class AdvertisementViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling Advertisement CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /brave/orders/api/v1/advertisements/ - List all advertisements (paginated)
    - POST /brave/orders/api/v1/advertisements/ - Create a new advertisement
    - GET /brave/orders/api/v1/advertisements/{id}/ - Retrieve a specific advertisement
    - PUT /brave/orders/api/v1/advertisements/{id}/ - Update an advertisement (full update)
    - PATCH /brave/orders/api/v1/advertisements/{id}/ - Update an advertisement (partial update)
    - DELETE /brave/orders/api/v1/advertisements/{id}/ - Delete an advertisement

    Attributes:
        queryset: The queryset of Advertisement objects to be used for the view.
            Returns all Advertisement instances.
        serializer_class: The serializer class to use for request/response
            serialization (AdvertisementSerializer).

    Examples using httpie CLI:
        # List all advertisements (paginated, 50 per page)
        http GET http://localhost:8000/brave/orders/api/v1/advertisements/

        # Create a new advertisement (requires existing order, element, kind)
        echo '{"order":1,"brand":"TechBrand","code":"AD-2024-001",' \\
            '"start_date":"2024-01-01","end_date":"2024-12-31",' \\
            '"quantity":100,"unit_price":"50.00",' \\
            '"advertisement_element":1,"advertisement_kind":1}' | \\
            http POST http://localhost:8000/brave/orders/api/v1/advertisements/ \\
            Content-Type:application/json

        # Retrieve a specific advertisement
        http GET http://localhost:8000/brave/orders/api/v1/advertisements/1/

        # Update an advertisement (full update)
        echo '{"order":1,"brand":"UpdatedBrand","code":"AD-2024-002",' \\
            '"start_date":"2024-02-01","end_date":"2024-12-31",' \\
            '"quantity":150,"unit_price":"75.00",' \\
            '"advertisement_element":1,"advertisement_kind":1}' | \\
            http PUT http://localhost:8000/brave/orders/api/v1/advertisements/1/ \\
            Content-Type:application/json

        # Partial update an advertisement
        echo '{"quantity":200}' | \\
            http PATCH http://localhost:8000/brave/orders/api/v1/advertisements/1/ \\
            Content-Type:application/json

        # Delete an advertisement
        http DELETE http://localhost:8000/brave/orders/api/v1/advertisements/1/
    """

    queryset: query.QuerySet[models.Advertisement] = (
        models.Advertisement.objects.all()  # pylint: disable=no-member
    )
    serializer_class: typing.Type[serializers.AdvertisementSerializer] = (
        serializers.AdvertisementSerializer
    )
    pagination_class: typing.Type[pagination.StandardResultsSetPagination] = (
        pagination.StandardResultsSetPagination
    )


class AdvertisementKindViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling AdvertisementKind CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /brave/orders/api/v1/advertisement-kinds/ - List all advertisement kinds (paginated)
    - POST /brave/orders/api/v1/advertisement-kinds/ - Create a new advertisement kind
    - GET /brave/orders/api/v1/advertisement-kinds/{id}/ - Retrieve a specific advertisement kind
    - PUT /brave/orders/api/v1/advertisement-kinds/{id}/ - Update an
        advertisement kind (full update)
    - PATCH /brave/orders/api/v1/advertisement-kinds/{id}/ - Update an
        advertisement kind (partial update)
    - DELETE /brave/orders/api/v1/advertisement-kinds/{id}/ - Delete an advertisement kind

    Attributes:
        queryset: The queryset of AdvertisementKind objects to be used for the view.
            Returns all AdvertisementKind instances.
        serializer_class: The serializer class to use for request/response
            serialization (AdvertisementKindSerializer).

    Examples using httpie CLI:
        # List all advertisement kinds (paginated, 50 per page)
        http GET http://localhost:8000/brave/orders/api/v1/advertisement-kinds/

        # Create a new advertisement kind
        echo '{"display_name":"Banner"}' | \\
            http POST http://localhost:8000/brave/orders/api/v1/advertisement-kinds/ \\
            Content-Type:application/json

        # Retrieve a specific advertisement kind
        http GET http://localhost:8000/brave/orders/api/v1/advertisement-kinds/1/

        # Update an advertisement kind (full update)
        echo '{"display_name":"Sidebar Banner"}' | \\
            http PUT http://localhost:8000/brave/orders/api/v1/advertisement-kinds/1/ \\
            Content-Type:application/json

        # Partial update an advertisement kind
        echo '{"display_name":"Updated Banner"}' | \\
            http PATCH http://localhost:8000/brave/orders/api/v1/advertisement-kinds/1/ \\
            Content-Type:application/json

        # Delete an advertisement kind
        http DELETE http://localhost:8000/brave/orders/api/v1/advertisement-kinds/1/
    """

    queryset: query.QuerySet[models.AdvertisementKind] = (
        models.AdvertisementKind.objects.all()  # pylint: disable=no-member
    )
    serializer_class: typing.Type[serializers.AdvertisementKindSerializer] = (
        serializers.AdvertisementKindSerializer
    )
    pagination_class: typing.Type[pagination.StandardResultsSetPagination] = (
        pagination.StandardResultsSetPagination
    )


class AdvertisementElementViewSet(
    viewsets.ModelViewSet
):  # pylint: disable=too-many-ancestors
    """ViewSet for handling AdvertisementElement CRUD operations via REST API.

    This ViewSet provides the following endpoints:
    - GET /brave/orders/api/v1/advertisement-elements/ - List all advertisement elements (paginated)
    - POST /brave/orders/api/v1/advertisement-elements/ - Create a new advertisement element
    - GET /brave/orders/api/v1/advertisement-elements/{id}/ - Retrieve a
        specific advertisement element
    - PUT /brave/orders/api/v1/advertisement-elements/{id}/ - Update an
        advertisement element (full update)
    - PATCH /brave/orders/api/v1/advertisement-elements/{id}/ - Update an
        advertisement element (partial update)
    - DELETE /brave/orders/api/v1/advertisement-elements/{id}/ - Delete an advertisement element

    Attributes:
        queryset: The queryset of AdvertisementElement objects to be used for the view.
            Returns all AdvertisementElement instances.
        serializer_class: The serializer class to use for request/response
            serialization (AdvertisementElementSerializer).

    Examples using httpie CLI:
        # List all advertisement elements (paginated, 50 per page)
        http GET http://localhost:8000/brave/orders/api/v1/advertisement-elements/

        # Create a new advertisement element
        echo '{"display":"Main Banner"}' | \\
            http POST http://localhost:8000/brave/orders/api/v1/advertisement-elements/ \\
            Content-Type:application/json

        # Retrieve a specific advertisement element
        http GET http://localhost:8000/brave/orders/api/v1/advertisement-elements/1/

        # Update an advertisement element (full update)
        echo '{"display":"Sidebar Banner"}' | \\
            http PUT http://localhost:8000/brave/orders/api/v1/advertisement-elements/1/ \\
            Content-Type:application/json

        # Partial update an advertisement element
        echo '{"display":"Updated Banner"}' | \\
            http PATCH http://localhost:8000/brave/orders/api/v1/advertisement-elements/1/ \\
            Content-Type:application/json

        # Delete an advertisement element
        http DELETE http://localhost:8000/brave/orders/api/v1/advertisement-elements/1/
    """

    queryset: query.QuerySet[models.AdvertisementElement] = (
        models.AdvertisementElement.objects.all()  # pylint: disable=no-member
    )
    serializer_class: typing.Type[
        serializers.AdvertisementElementSerializer
    ] = serializers.AdvertisementElementSerializer
    pagination_class: typing.Type[pagination.StandardResultsSetPagination] = (
        pagination.StandardResultsSetPagination
    )
