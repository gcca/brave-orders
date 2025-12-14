"""Django models for the brave_orders application."""

import django.db.models as models  # pylint: disable=consider-using-from-import


class Customer(models.Model):
    """Customer model representing a client in the system.

    This model stores comprehensive customer information including identification
    details, contact information, and metadata for tracking creation and updates.

    Attributes:
        name (CharField): The full name of the customer company or individual.
            Maximum length is 255 characters.
        ruc (CharField): The RUC (Registro Único de Contribuyente) tax identification
            number. Must be unique. Maximum length is 20 characters.
        email (EmailField): The primary email address for the customer.
        phone (CharField): The primary phone number for the customer.
            Maximum length is 20 characters.
        address (TextField): The complete address of the customer.
        contact_name (CharField): The name of the primary contact person
            for this customer. Maximum length is 255 characters.
        created_at (DateTimeField): Timestamp indicating when the customer record
            was created. Automatically set on creation.
        updated_at (DateTimeField): Timestamp indicating when the customer record
            was last modified. Automatically updated on each save.

    Example:
        >>> customer = Customer.objects.create(
        ...     name="Acme Corp",
        ...     ruc="12345678901",
        ...     email="contact@acme.com",
        ...     phone="+1234567890",
        ...     address="123 Main St",
        ...     contact_name="John Doe"
        ... )
        >>> str(customer)
        'Acme Corp'
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="The full name of the customer company or individual.",
    )
    ruc = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="RUC",
        help_text=(
            "The RUC (Registro Único de Contribuyente) tax identification "
            "number. Must be unique."
        ),
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="The primary email address for the customer.",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone",
        help_text="The primary phone number for the customer.",
    )
    address = models.TextField(
        verbose_name="Address",
        help_text="The complete address of the customer.",
    )
    contact_name = models.CharField(
        max_length=255,
        verbose_name="Contact Name",
        help_text="The name of the primary contact person for this customer.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="Timestamp indicating when the customer record was created.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At",
        help_text="Timestamp indicating when the customer record was last modified.",
    )

    def __str__(self) -> str:
        """Return a string representation of the Customer instance.

        Returns:
            str: The name of the customer.
        """
        return str(self.name)


class Seller(models.Model):
    """Seller model representing a vendor or supplier in the system.

    This model stores comprehensive seller information including personal details,
    company information, and contact data for vendors and suppliers.

    Attributes:
        name (CharField): The full name of the seller or sales representative.
            Maximum length is 255 characters.
        address (TextField): The complete address of the seller.
        email (EmailField): The primary email address for the seller.
        company_name (CharField): The name of the company the seller represents.
            Maximum length is 255 characters.
        ruc (CharField): The RUC (Registro Único de Contribuyente) tax
            identification number of the seller's company. Maximum length is 20 characters.

    Example:
        >>> seller = Seller.objects.create(
        ...     name="Jane Smith",
        ...     address="456 Business Ave",
        ...     email="jane@example.com",
        ...     company_name="Tech Solutions Inc",
        ...     ruc="98765432109"
        ... )
        >>> str(seller)
        'Jane Smith'
    """

    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="The full name of the seller or sales representative.",
    )
    address = models.TextField(
        verbose_name="Address",
        help_text="The complete address of the seller.",
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="The primary email address for the seller.",
    )
    company_name = models.CharField(
        max_length=255,
        verbose_name="Company Name",
        help_text="The name of the company the seller represents.",
    )
    ruc = models.CharField(
        max_length=20,
        verbose_name="RUC",
        help_text=(
            "The RUC (Registro Único de Contribuyente) tax identification "
            "number of the seller's company."
        ),
    )

    def __str__(self) -> str:
        """Return a string representation of the Seller instance.

        Returns:
            str: The name of the seller.
        """
        return str(self.name)


class Order(models.Model):
    """Order model representing a purchase order in the system.

    This model stores order information including customer relationship,
    contact details, and payment terms for purchase orders.

    Attributes:
        customer (ForeignKey): Reference to the Customer who placed the order.
            Uses PROTECT deletion - prevents deletion if orders exist.
        seller (ForeignKey): Reference to the Seller who is fulfilling the order.
            Uses PROTECT deletion - prevents deletion if orders exist.
        ruc (CharField): The RUC (Registro Único de Contribuyente) tax
            identification number for the order. Maximum length is 20 characters.
        email (EmailField): The email address associated with the order.
        address (TextField): The delivery or billing address for the order.
        phone (CharField): The phone number associated with the order.
            Maximum length is 20 characters.
        contact_name (CharField): The name of the contact person for this order.
            Maximum length is 255 characters.
        payment_days (PositiveIntegerField): The number of days for payment
            terms for the order. Must be a positive integer value.

    Example:
        >>> customer = Customer.objects.create(name="Acme Corp", ruc="12345678901",
        ...     email="contact@acme.com", phone="+1234567890", address="123 Main St",
        ...     contact_name="John Doe")
        >>> seller = Seller.objects.create(name="Jane Smith", address="456 Business Ave",
        ...     email="jane@example.com", company_name="Tech Solutions Inc", ruc="98765432109")
        >>> order = Order.objects.create(
        ...     customer=customer,
        ...     seller=seller,
        ...     ruc="12345678901",
        ...     email="orders@acme.com",
        ...     address="123 Main St",
        ...     phone="+1234567890",
        ...     contact_name="John Doe",
        ...     payment_days=30
        ... )
        >>> str(order)
        'Order for Acme Corp'
    """

    customer = models.ForeignKey(
        "Customer",
        on_delete=models.PROTECT,
        verbose_name="Customer",
        help_text="The customer who placed this order.",
        related_name="orders",
    )
    seller = models.ForeignKey(
        "Seller",
        on_delete=models.PROTECT,
        verbose_name="Seller",
        help_text="The seller who is fulfilling this order.",
        related_name="orders",
    )
    ruc = models.CharField(
        max_length=20,
        verbose_name="RUC",
        help_text=(
            "The RUC (Registro Único de Contribuyente) tax identification "
            "number for the order."
        ),
    )
    email = models.EmailField(
        verbose_name="Email",
        help_text="The email address associated with the order.",
    )
    address = models.TextField(
        verbose_name="Address",
        help_text="The delivery or billing address for the order.",
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Phone",
        help_text="The phone number associated with the order.",
    )
    contact_name = models.CharField(
        max_length=255,
        verbose_name="Contact Name",
        help_text="The name of the contact person for this order.",
    )
    payment_days = models.PositiveIntegerField(
        verbose_name="Payment Days",
        help_text="The number of days for payment terms for the order. Must be a positive integer.",
    )

    def __str__(self) -> str:
        """Return a string representation of the Order instance.

        Returns:
            str: A string indicating the order and associated customer name.
        """
        return f"Order for {self.customer.name}"


class Advertisement(models.Model):
    """Advertisement model representing advertising items in orders.

    This model stores advertising information associated with orders, including
    brand details, codes, date ranges, quantities, and pricing information.

    Attributes:
        order (ForeignKey): Reference to the Order that contains this advertisement.
            Uses PROTECT deletion - prevents deletion if advertisements exist.
        brand (CharField): The brand name associated with the advertisement.
            Maximum length is 255 characters.
        code (CharField): The code or identifier for the advertisement.
            Maximum length is 100 characters.
        start_date (DateField): The start date when the advertisement begins.
        end_date (DateField): The end date when the advertisement expires.
        quantity (PositiveIntegerField): The quantity of advertisement units.
            Must be a positive integer value.
        unit_price (DecimalField): The unit price for each advertisement item.
            Maximum 10 digits with 2 decimal places.
        advertisement_element (ForeignKey): Reference to the AdvertisementElement
            associated with this advertisement. Uses PROTECT deletion - prevents
            deletion if advertisements exist.
        advertisement_kind (ForeignKey): Reference to the AdvertisementKind
            associated with this advertisement. Uses PROTECT deletion - prevents
            deletion if advertisements exist.

    Example:
        >>> customer = Customer.objects.create(name="Acme Corp", ruc="12345678901",
        ...     email="contact@acme.com", phone="+1234567890", address="123 Main St",
        ...     contact_name="John Doe")
        >>> seller = Seller.objects.create(name="Jane Smith", address="456 Business Ave",
        ...     email="jane@example.com", company_name="Tech Solutions Inc", ruc="98765432109")
        >>> order = Order.objects.create(customer=customer, seller=seller, ruc="12345678901",
        ...     email="orders@acme.com", address="123 Main St", phone="+1234567890",
        ...     contact_name="John Doe", payment_days=30)
        >>> element = AdvertisementElement.objects.create(display="Main Banner")
        >>> kind = AdvertisementKind.objects.create(display_name="Banner")
        >>> advertisement = Advertisement.objects.create(
        ...     order=order,
        ...     brand="TechBrand",
        ...     code="AD-2024-001",
        ...     start_date="2024-01-01",
        ...     end_date="2024-12-31",
        ...     quantity=100,
        ...     unit_price=50.00,
        ...     advertisement_element=element,
        ...     advertisement_kind=kind
        ... )
        >>> str(advertisement)
        'TechBrand - AD-2024-001'
    """

    order = models.ForeignKey(
        "Order",
        on_delete=models.PROTECT,
        verbose_name="Order",
        help_text="The order that contains this advertisement.",
        related_name="advertisements",
    )
    brand = models.CharField(
        max_length=255,
        verbose_name="Brand",
        help_text="The brand name associated with the advertisement.",
    )
    code = models.CharField(
        max_length=100,
        verbose_name="Code",
        help_text="The code or identifier for the advertisement.",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
        help_text="The start date when the advertisement begins.",
    )
    end_date = models.DateField(
        verbose_name="End Date",
        help_text="The end date when the advertisement expires.",
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Quantity",
        help_text="The quantity of advertisement units. Must be a positive integer.",
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Unit Price",
        help_text="The unit price for each advertisement item.",
    )
    advertisement_element = models.ForeignKey(
        "AdvertisementElement",
        on_delete=models.PROTECT,
        verbose_name="Advertisement Element",
        help_text="The advertisement element associated with this advertisement.",
        related_name="advertisements",
    )
    advertisement_kind = models.ForeignKey(
        "AdvertisementKind",
        on_delete=models.PROTECT,
        verbose_name="Advertisement Kind",
        help_text="The advertisement kind associated with this advertisement.",
        related_name="advertisements",
    )

    def __str__(self) -> str:
        """Return a string representation of the Advertisement instance.

        Returns:
            str: A string combining the brand name and code.
        """
        return f"{self.brand} - {self.code}"


class AdvertisementKind(models.Model):
    """Advertisement Kind model representing types or categories of advertisements.

    This model stores different kinds or categories of advertisements that can
    be used to classify and organize advertisement elements.

    Attributes:
        display_name (CharField): The display name for the advertisement kind.
            Maximum length is 255 characters.

    Example:
        >>> kind = AdvertisementKind.objects.create(display_name="Banner")
        >>> str(kind)
        'Banner'
    """

    display_name = models.CharField(
        max_length=255,
        verbose_name="Display Name",
        help_text="The display name for the advertisement kind.",
    )

    def __str__(self) -> str:
        """Return a string representation of the AdvertisementKind instance.

        Returns:
            str: The display name of the advertisement kind.
        """
        return str(self.display_name)


class AdvertisementElement(models.Model):
    """Advertisement Element model representing individual advertisement elements.

    This model stores individual advertisement elements with display information
    for rendering or presentation purposes.

    Attributes:
        display (CharField): The display text or identifier for the advertisement element.
            Maximum length is 255 characters.

    Example:
        >>> element = AdvertisementElement.objects.create(display="Main Banner")
        >>> str(element)
        'Main Banner'
    """

    display = models.CharField(
        max_length=255,
        verbose_name="Display",
        help_text="The display text or identifier for the advertisement element.",
    )

    def __str__(self) -> str:
        """Return a string representation of the AdvertisementElement instance.

        Returns:
            str: The display text of the advertisement element.
        """
        return str(self.display)
