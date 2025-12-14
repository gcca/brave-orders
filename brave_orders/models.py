"""Django models for the brave_orders application."""

from django.db import models


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
        company_ruc (CharField): The RUC (Registro Único de Contribuyente) tax
            identification number of the seller's company. Maximum length is 20 characters.

    Example:
        >>> seller = Seller.objects.create(
        ...     name="Jane Smith",
        ...     address="456 Business Ave",
        ...     email="jane@example.com",
        ...     company_name="Tech Solutions Inc",
        ...     company_ruc="98765432109"
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
    company_ruc = models.CharField(
        max_length=20,
        verbose_name="Company RUC",
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
