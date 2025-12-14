"""Django REST Framework serializers for the brave_orders application."""

import rest_framework.serializers as serializers  # pylint: disable=consider-using-from-import

import brave_orders.models as models  # pylint: disable=consider-using-from-import


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


class SellerSerializer(
    serializers.ModelSerializer
):  # pylint: disable=too-few-public-methods
    """Serializer for the Seller model.

    This serializer handles serialization and deserialization of Seller instances
    for API requests and responses. It includes all fields from the Seller model
    and provides validation for the data.

    Attributes:
        Meta.model: The Django model class to serialize (Seller).
        Meta.fields: Specifies that all model fields should be included in the
            serialization.

    Example:
        >>> serializer = SellerSerializer(data={
        ...     'name': 'Jane Smith',
        ...     'address': '456 Business Ave',
        ...     'email': 'jane@example.com',
        ...     'company_name': 'Tech Solutions Inc',
        ...     'ruc': '98765432109'
        ... })
        >>> serializer.is_valid()
        True
        >>> seller = serializer.save()
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta configuration for SellerSerializer."""

        model = models.Seller
        fields = "__all__"


class OrderSerializer(
    serializers.ModelSerializer
):  # pylint: disable=too-few-public-methods
    """Serializer for the Order model.

    This serializer handles serialization and deserialization of Order instances
    for API requests and responses. It includes all fields from the Order model
    and provides validation for the data.

    Attributes:
        Meta.model: The Django model class to serialize (Order).
        Meta.fields: Specifies that all model fields should be included in the
            serialization.

    Example:
        >>> serializer = OrderSerializer(data={
        ...     'customer': 1,
        ...     'seller': 1,
        ...     'ruc': '12345678901',
        ...     'email': 'orders@acme.com',
        ...     'address': '123 Main St',
        ...     'phone': '+1234567890',
        ...     'contact_name': 'John Doe',
        ...     'payment_days': 30
        ... })
        >>> serializer.is_valid()
        True
        >>> order = serializer.save()
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta configuration for OrderSerializer."""

        model = models.Order
        fields = "__all__"


class AdvertisementSerializer(
    serializers.ModelSerializer
):  # pylint: disable=too-few-public-methods
    """Serializer for the Advertisement model.

    This serializer handles serialization and deserialization of Advertisement
    instances for API requests and responses. It includes all fields from the
    Advertisement model and provides validation for the data.

    Attributes:
        Meta.model: The Django model class to serialize (Advertisement).
        Meta.fields: Specifies that all model fields should be included in the
            serialization.

    Example:
        >>> serializer = AdvertisementSerializer(data={
        ...     'order': 1,
        ...     'brand': 'TechBrand',
        ...     'code': 'AD-2024-001',
        ...     'start_date': '2024-01-01',
        ...     'end_date': '2024-12-31',
        ...     'quantity': 100,
        ...     'unit_price': '50.00',
        ...     'advertisement_element': 1,
        ...     'advertisement_kind': 1
        ... })
        >>> serializer.is_valid()
        True
        >>> advertisement = serializer.save()
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta configuration for AdvertisementSerializer."""

        model = models.Advertisement
        fields = "__all__"


class AdvertisementKindSerializer(
    serializers.ModelSerializer
):  # pylint: disable=too-few-public-methods
    """Serializer for the AdvertisementKind model.

    This serializer handles serialization and deserialization of AdvertisementKind
    instances for API requests and responses. It includes all fields from the
    AdvertisementKind model and provides validation for the data.

    Attributes:
        Meta.model: The Django model class to serialize (AdvertisementKind).
        Meta.fields: Specifies that all model fields should be included in the
            serialization.

    Example:
        >>> serializer = AdvertisementKindSerializer(data={
        ...     'display_name': 'Banner'
        ... })
        >>> serializer.is_valid()
        True
        >>> kind = serializer.save()
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta configuration for AdvertisementKindSerializer."""

        model = models.AdvertisementKind
        fields = "__all__"


class AdvertisementElementSerializer(
    serializers.ModelSerializer
):  # pylint: disable=too-few-public-methods
    """Serializer for the AdvertisementElement model.

    This serializer handles serialization and deserialization of AdvertisementElement
    instances for API requests and responses. It includes all fields from the
    AdvertisementElement model and provides validation for the data.

    Attributes:
        Meta.model: The Django model class to serialize (AdvertisementElement).
        Meta.fields: Specifies that all model fields should be included in the
            serialization.

    Example:
        >>> serializer = AdvertisementElementSerializer(data={
        ...     'display': 'Main Banner'
        ... })
        >>> serializer.is_valid()
        True
        >>> element = serializer.save()
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """Meta configuration for AdvertisementElementSerializer."""

        model = models.AdvertisementElement
        fields = "__all__"
