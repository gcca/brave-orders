from django.db import models


class Customer(models.Model):
    """Model to handle customer information."""

    name = models.CharField(max_length=255, verbose_name="Name")
    ruc = models.CharField(max_length=20, unique=True, verbose_name="RUC")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Phone")
    address = models.TextField(verbose_name="Address")
    contact_name = models.CharField(max_length=255, verbose_name="Contact Name")

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At"
    )
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
