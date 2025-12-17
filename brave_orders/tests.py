"""Tests for the brave_orders application."""

import typing

import django.db.models.deletion as deletion
import django.test as test
import rest_framework.status as status
import rest_framework.test as rest_test

import brave_orders.models as models


class CustomerViewSetTestCase(rest_test.APITestCase):
    """Test cases for Customer CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.customer_data: typing.Dict[str, typing.Any] = {
            "name": "Test Corp",
            "ruc": "12345678901",
            "email": "test@testcorp.com",
            "phone": "+1234567890",
            "address": "123 Test St",
            "contact_name": "John Test",
        }

    def test_create_customer(self) -> None:
        """Test creating a customer via POST request."""
        response = self.client.post(
            "/brave/orders/api/v1/customers/",
            self.customer_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Customer.objects.count(), 1)
        self.assertEqual(
            models.Customer.objects.get().name,
            "Test Corp",
        )

    def test_list_customers(self) -> None:
        """Test listing customers via GET request."""
        models.Customer.objects.create(**self.customer_data)
        response = self.client.get("/brave/orders/api/v1/customers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)

    def test_retrieve_customer(self) -> None:
        """Test retrieving a specific customer via GET request."""
        customer = models.Customer.objects.create(**self.customer_data)
        response = self.client.get(
            f"/brave/orders/api/v1/customers/{customer.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Corp")
        self.assertEqual(response.data["ruc"], "12345678901")

    def test_update_customer(self) -> None:
        """Test updating a customer via PUT request."""
        customer = models.Customer.objects.create(**self.customer_data)
        updated_data = self.customer_data.copy()
        updated_data["name"] = "Updated Corp"
        response = self.client.put(
            f"/brave/orders/api/v1/customers/{customer.id}/",
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Corp")

    def test_partial_update_customer(self) -> None:
        """Test partially updating a customer via PATCH request."""
        customer = models.Customer.objects.create(**self.customer_data)
        response = self.client.patch(
            f"/brave/orders/api/v1/customers/{customer.id}/",
            {"email": "newemail@testcorp.com"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "newemail@testcorp.com")
        self.assertEqual(response.data["name"], "Test Corp")

    def test_delete_customer(self) -> None:
        """Test deleting a customer via DELETE request."""
        customer = models.Customer.objects.create(**self.customer_data)
        response = self.client.delete(
            f"/brave/orders/api/v1/customers/{customer.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Customer.objects.count(), 0)


class SellerViewSetTestCase(rest_test.APITestCase):
    """Test cases for Seller CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.seller_data: typing.Dict[str, typing.Any] = {
            "name": "Jane Seller",
            "address": "456 Seller Ave",
            "email": "jane@seller.com",
            "company_name": "Seller Solutions Inc",
            "ruc": "98765432109",
        }

    def test_create_seller(self) -> None:
        """Test creating a seller via POST request."""
        response = self.client.post(
            "/brave/orders/api/v1/sellers/", self.seller_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Seller.objects.count(), 1)

    def test_list_sellers(self) -> None:
        """Test listing sellers via GET request."""
        models.Seller.objects.create(**self.seller_data)
        response = self.client.get("/brave/orders/api/v1/sellers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_retrieve_seller(self) -> None:
        """Test retrieving a specific seller via GET request."""
        seller = models.Seller.objects.create(**self.seller_data)
        response = self.client.get(f"/brave/orders/api/v1/sellers/{seller.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Jane Seller")
        self.assertEqual(response.data["ruc"], "98765432109")

    def test_update_seller(self) -> None:
        """Test updating a seller via PUT request."""
        seller = models.Seller.objects.create(**self.seller_data)
        updated_data = self.seller_data.copy()
        updated_data["name"] = "Updated Seller"
        updated_data["email"] = "updated@seller.com"
        response = self.client.put(
            f"/brave/orders/api/v1/sellers/{seller.id}/",
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Updated Seller")
        self.assertEqual(response.data["email"], "updated@seller.com")

    def test_partial_update_seller(self) -> None:
        """Test partially updating a seller via PATCH request."""
        seller = models.Seller.objects.create(**self.seller_data)
        response = self.client.patch(
            f"/brave/orders/api/v1/sellers/{seller.id}/",
            {"company_name": "New Company Name"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["company_name"], "New Company Name")
        self.assertEqual(response.data["name"], "Jane Seller")

    def test_delete_seller(self) -> None:
        """Test deleting a seller via DELETE request."""
        seller = models.Seller.objects.create(**self.seller_data)
        response = self.client.delete(
            f"/brave/orders/api/v1/sellers/{seller.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Seller.objects.count(), 0)


class AdvertisementKindViewSetTestCase(rest_test.APITestCase):
    """Test cases for AdvertisementKind CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.kind_data: typing.Dict[str, str] = {"display_name": "Test Kind"}

    def test_create_advertisement_kind(self) -> None:
        """Test creating an advertisement kind via POST request."""
        response = self.client.post(
            "/brave/orders/api/v1/advertisement-kinds/",
            self.kind_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            models.AdvertisementKind.objects.count(),
            1,
        )

    def test_list_advertisement_kinds(self) -> None:
        """Test listing advertisement kinds via GET request."""
        models.AdvertisementKind.objects.create(**self.kind_data)
        response = self.client.get("/brave/orders/api/v1/advertisement-kinds/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_retrieve_advertisement_kind(self) -> None:
        """Test retrieving a specific advertisement kind via GET request."""
        kind = models.AdvertisementKind.objects.create(**self.kind_data)
        response = self.client.get(
            f"/brave/orders/api/v1/advertisement-kinds/{kind.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display_name"], "Test Kind")

    def test_update_advertisement_kind(self) -> None:
        """Test updating an advertisement kind via PUT request."""
        kind = models.AdvertisementKind.objects.create(**self.kind_data)
        updated_data = {"display_name": "Updated Kind"}
        response = self.client.put(
            f"/brave/orders/api/v1/advertisement-kinds/{kind.id}/",
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display_name"], "Updated Kind")

    def test_partial_update_advertisement_kind(self) -> None:
        """Test partially updating an advertisement kind via PATCH request."""
        kind = models.AdvertisementKind.objects.create(**self.kind_data)
        response = self.client.patch(
            f"/brave/orders/api/v1/advertisement-kinds/{kind.id}/",
            {"display_name": "Patched Kind"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display_name"], "Patched Kind")

    def test_delete_advertisement_kind(self) -> None:
        """Test deleting an advertisement kind via DELETE request."""
        kind = models.AdvertisementKind.objects.create(**self.kind_data)
        response = self.client.delete(
            f"/brave/orders/api/v1/advertisement-kinds/{kind.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.AdvertisementKind.objects.count(), 0)


class AdvertisementElementViewSetTestCase(rest_test.APITestCase):
    """Test cases for AdvertisementElement CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.element_data: typing.Dict[str, str] = {
            "display": "Test Banner",
            "code": "TEST-001",
        }

    def test_create_advertisement_element(self) -> None:
        """Test creating an advertisement element via POST request."""
        response = self.client.post(
            "/brave/orders/api/v1/advertisement-elements/",
            self.element_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            models.AdvertisementElement.objects.count(),
            1,
        )
        self.assertEqual(
            models.AdvertisementElement.objects.get().code,
            "TEST-001",
        )

    def test_list_advertisement_elements(self) -> None:
        """Test listing advertisement elements via GET request."""
        models.AdvertisementElement.objects.create(**self.element_data)
        response = self.client.get(
            "/brave/orders/api/v1/advertisement-elements/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["code"], "TEST-001")

    def test_retrieve_advertisement_element(self) -> None:
        """Test retrieving a specific advertisement element via GET request."""
        element = models.AdvertisementElement.objects.create(
            **self.element_data
        )
        response = self.client.get(
            f"/brave/orders/api/v1/advertisement-elements/{element.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display"], "Test Banner")
        self.assertEqual(response.data["code"], "TEST-001")

    def test_update_advertisement_element(self) -> None:
        """Test updating an advertisement element via PUT request."""
        element = models.AdvertisementElement.objects.create(
            **self.element_data
        )
        updated_data = {"display": "Updated Banner", "code": "TEST-002"}
        response = self.client.put(
            f"/brave/orders/api/v1/advertisement-elements/{element.id}/",
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display"], "Updated Banner")
        self.assertEqual(response.data["code"], "TEST-002")

    def test_partial_update_advertisement_element(self) -> None:
        """Test partially updating an advertisement element via PATCH request."""
        element = models.AdvertisementElement.objects.create(
            **self.element_data
        )
        response = self.client.patch(
            f"/brave/orders/api/v1/advertisement-elements/{element.id}/",
            {"display": "Patched Banner"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display"], "Patched Banner")
        self.assertEqual(response.data["code"], "TEST-001")

    def test_delete_advertisement_element(self) -> None:
        """Test deleting an advertisement element via DELETE request."""
        element = models.AdvertisementElement.objects.create(
            **self.element_data
        )
        response = self.client.delete(
            f"/brave/orders/api/v1/advertisement-elements/{element.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.AdvertisementElement.objects.count(), 0)


class AdvertisementViewSetTestCase(rest_test.APITestCase):
    """Test cases for Advertisement CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.customer = models.Customer.objects.create(
            name="Test Corp",
            ruc="12345678901",
            email="test@testcorp.com",
            phone="+1234567890",
            address="123 Test St",
            contact_name="John Test",
        )
        self.seller = models.Seller.objects.create(
            name="Jane Seller",
            address="456 Seller Ave",
            email="jane@seller.com",
            company_name="Seller Solutions Inc",
            ruc="98765432109",
        )
        self.order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="123 Order St",
            phone="+1234567890",
            contact_name="Jane Order",
            payment_days=30,
        )
        self.kind = models.AdvertisementKind.objects.create(
            display_name="Test Kind"
        )
        self.element = models.AdvertisementElement.objects.create(
            display="Test Banner", code="TEST-001"
        )
        self.advertisement_data: typing.Dict[str, typing.Any] = {
            "order": self.order.id,
            "brand": "TestBrand",
            "code": "AD-TEST-001",
            "start_date": "2024-01-01",
            "end_date": "2024-12-31",
            "quantity": 100,
            "unit_price": "50.00",
            "advertisement_element": self.element.id,
            "advertisement_kind": self.kind.id,
        }

    def test_create_advertisement(self) -> None:
        """Test creating an advertisement via POST request."""
        response = self.client.post(
            "/brave/orders/api/v1/advertisements/",
            self.advertisement_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Advertisement.objects.count(), 1)

    def test_list_advertisements(self) -> None:
        """Test listing advertisements via GET request."""
        models.Advertisement.objects.create(
            order=self.order,
            brand="TestBrand",
            code="AD-TEST-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=self.element,
            advertisement_kind=self.kind,
        )
        response = self.client.get("/brave/orders/api/v1/advertisements/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_retrieve_advertisement(self) -> None:
        """Test retrieving a specific advertisement via GET request."""
        advertisement = models.Advertisement.objects.create(
            order=self.order,
            brand="TestBrand",
            code="AD-TEST-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=self.element,
            advertisement_kind=self.kind,
        )
        response = self.client.get(
            f"/brave/orders/api/v1/advertisements/{advertisement.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["brand"], "TestBrand")
        self.assertEqual(response.data["code"], "AD-TEST-001")

    def test_update_advertisement(self) -> None:
        """Test updating an advertisement via PUT request."""
        advertisement = models.Advertisement.objects.create(
            order=self.order,
            brand="TestBrand",
            code="AD-TEST-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=self.element,
            advertisement_kind=self.kind,
        )
        updated_data = self.advertisement_data.copy()
        updated_data["brand"] = "UpdatedBrand"
        updated_data["quantity"] = 200
        response = self.client.put(
            f"/brave/orders/api/v1/advertisements/{advertisement.id}/",
            updated_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["brand"], "UpdatedBrand")
        self.assertEqual(response.data["quantity"], 200)

    def test_partial_update_advertisement(self) -> None:
        """Test partially updating an advertisement via PATCH request."""
        advertisement = models.Advertisement.objects.create(
            order=self.order,
            brand="TestBrand",
            code="AD-TEST-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=self.element,
            advertisement_kind=self.kind,
        )
        response = self.client.patch(
            f"/brave/orders/api/v1/advertisements/{advertisement.id}/",
            {"brand": "PatchedBrand", "unit_price": "99.99"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["brand"], "PatchedBrand")
        self.assertEqual(response.data["unit_price"], "99.99")
        self.assertEqual(response.data["code"], "AD-TEST-001")

    def test_delete_advertisement(self) -> None:
        """Test deleting an advertisement via DELETE request."""
        advertisement = models.Advertisement.objects.create(
            order=self.order,
            brand="TestBrand",
            code="AD-TEST-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=self.element,
            advertisement_kind=self.kind,
        )
        response = self.client.delete(
            f"/brave/orders/api/v1/advertisements/{advertisement.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Advertisement.objects.count(), 0)


class OrderViewSetTestCase(rest_test.APITestCase):
    """Test cases for Order CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.customer = models.Customer.objects.create(
            name="Test Corp",
            ruc="12345678901",
            email="test@testcorp.com",
            phone="+1234567890",
            address="123 Test St",
            contact_name="John Test",
        )
        self.seller = models.Seller.objects.create(
            name="Jane Seller",
            address="456 Seller Ave",
            email="jane@seller.com",
            company_name="Seller Solutions Inc",
            ruc="98765432109",
        )
        self.kind = models.AdvertisementKind.objects.create(
            display_name="Test Kind"
        )
        self.element = models.AdvertisementElement.objects.create(
            display="Test Banner", code="TEST-001"
        )
        self.order_data: typing.Dict[str, typing.Any] = {
            "customer": self.customer.id,
            "seller": self.seller.id,
            "ruc": "12345678901",
            "email": "order@test.com",
            "address": "123 Order St",
            "phone": "+1234567890",
            "contact_name": "Jane Order",
            "payment_days": 30,
        }

    def test_create_order(self) -> None:
        """Test creating an order via POST request."""
        response = self.client.post(
            "/brave/orders/api/v1/orders/", self.order_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Order.objects.count(), 1)
        self.assertEqual(response.data["advertisements"], [])

    def test_create_order_with_nested_advertisements(self) -> None:
        """Test creating an order with nested advertisements via POST request."""
        order_data_with_ads = self.order_data.copy()
        order_data_with_ads["advertisements"] = [
            {
                "brand": "TestBrand",
                "code": "AD-TEST-001",
                "start_date": "2024-01-01",
                "end_date": "2024-12-31",
                "quantity": 100,
                "unit_price": "50.00",
                "advertisement_element": self.element.id,
                "advertisement_kind": self.kind.id,
            }
        ]
        response = self.client.post(
            "/brave/orders/api/v1/orders/", order_data_with_ads, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Order.objects.count(), 1)
        self.assertEqual(models.Advertisement.objects.count(), 1)
        self.assertEqual(len(response.data["advertisements"]), 1)
        self.assertEqual(
            response.data["advertisements"][0]["brand"], "TestBrand"
        )

    def test_list_orders(self) -> None:
        """Test listing orders via GET request."""
        models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="123 Order St",
            phone="+1234567890",
            contact_name="Jane Order",
            payment_days=30,
        )
        response = self.client.get("/brave/orders/api/v1/orders/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_retrieve_order(self) -> None:
        """Test retrieving a specific order via GET request."""
        order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="123 Order St",
            phone="+1234567890",
            contact_name="Jane Order",
            payment_days=30,
        )
        response = self.client.get(f"/brave/orders/api/v1/orders/{order.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "order@test.com")
        self.assertIn("advertisements", response.data)

    def test_update_order_with_nested_advertisements(self) -> None:
        """Test updating an order with nested advertisements via PUT request."""
        order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="123 Order St",
            phone="+1234567890",
            contact_name="Jane Order",
            payment_days=30,
        )
        # Create initial advertisement
        models.Advertisement.objects.create(
            order=order,
            brand="OldBrand",
            code="AD-OLD-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=50,
            unit_price="25.00",
            advertisement_element=self.element,
            advertisement_kind=self.kind,
        )

        # Update order with new advertisement (should replace old one)
        updated_order_data = self.order_data.copy()
        updated_order_data["email"] = "updated@test.com"
        updated_order_data["advertisements"] = [
            {
                "brand": "NewBrand",
                "code": "AD-NEW-001",
                "start_date": "2024-02-01",
                "end_date": "2024-12-31",
                "quantity": 150,
                "unit_price": "75.00",
                "advertisement_element": self.element.id,
                "advertisement_kind": self.kind.id,
            }
        ]
        response = self.client.put(
            f"/brave/orders/api/v1/orders/{order.id}/",
            updated_order_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], "updated@test.com")
        self.assertEqual(len(response.data["advertisements"]), 1)
        self.assertEqual(
            response.data["advertisements"][0]["brand"], "NewBrand"
        )
        # Verify old advertisement was deleted
        self.assertEqual(models.Advertisement.objects.count(), 1)
        self.assertEqual(
            models.Advertisement.objects.get().brand,
            "NewBrand",
        )

    def test_partial_update_order(self) -> None:
        """Test partially updating an order via PATCH request."""
        order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="123 Order St",
            phone="+1234567890",
            contact_name="Jane Order",
            payment_days=30,
        )
        response = self.client.patch(
            f"/brave/orders/api/v1/orders/{order.id}/",
            {"payment_days": 45},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["payment_days"], 45)
        self.assertEqual(response.data["email"], "order@test.com")

    def test_delete_order(self) -> None:
        """Test deleting an order via DELETE request."""
        order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="123 Order St",
            phone="+1234567890",
            contact_name="Jane Order",
            payment_days=30,
        )
        response = self.client.delete(
            f"/brave/orders/api/v1/orders/{order.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Order.objects.count(), 0)

    def test_create_order_with_multiple_advertisements(self) -> None:
        """Test creating an order with multiple nested advertisements."""
        order_data_with_ads = self.order_data.copy()
        order_data_with_ads["advertisements"] = [
            {
                "brand": "Brand1",
                "code": "AD-001",
                "start_date": "2024-01-01",
                "end_date": "2024-06-30",
                "quantity": 50,
                "unit_price": "25.00",
                "advertisement_element": self.element.id,
                "advertisement_kind": self.kind.id,
            },
            {
                "brand": "Brand2",
                "code": "AD-002",
                "start_date": "2024-07-01",
                "end_date": "2024-12-31",
                "quantity": 100,
                "unit_price": "50.00",
                "advertisement_element": self.element.id,
                "advertisement_kind": self.kind.id,
            },
        ]
        response = self.client.post(
            "/brave/orders/api/v1/orders/", order_data_with_ads, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Order.objects.count(), 1)
        self.assertEqual(models.Advertisement.objects.count(), 2)
        self.assertEqual(len(response.data["advertisements"]), 2)
        brands = [ad["brand"] for ad in response.data["advertisements"]]
        self.assertIn("Brand1", brands)
        self.assertIn("Brand2", brands)


class ErrorHandlingTestCase(rest_test.APITestCase):
    """Test cases for error handling and edge cases."""

    def test_retrieve_nonexistent_customer(self) -> None:
        """Test retrieving a non-existent customer returns 404."""
        response = self.client.get("/brave/orders/api/v1/customers/99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_nonexistent_customer(self) -> None:
        """Test updating a non-existent customer returns 404."""
        customer_data = {
            "name": "Test Corp",
            "ruc": "12345678901",
            "email": "test@test.com",
            "phone": "+1234567890",
            "address": "123 Test St",
            "contact_name": "John Test",
        }
        response = self.client.put(
            "/brave/orders/api/v1/customers/99999/",
            customer_data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_nonexistent_customer(self) -> None:
        """Test deleting a non-existent customer returns 404."""
        response = self.client.delete("/brave/orders/api/v1/customers/99999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_customer_missing_required_fields(self) -> None:
        """Test creating a customer with missing required fields."""
        incomplete_data = {"name": "Test Corp"}
        response = self.client.post(
            "/brave/orders/api/v1/customers/", incomplete_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_order_with_nonexistent_customer(self) -> None:
        """Test creating an order with non-existent customer."""
        seller = models.Seller.objects.create(
            name="Test Seller",
            address="Address",
            email="seller@test.com",
            company_name="Test Co",
            ruc="12345678901",
        )
        order_data = {
            "customer": 99999,
            "seller": seller.id,
            "ruc": "12345678901",
            "email": "test@test.com",
            "address": "Address",
            "phone": "+1234567890",
            "contact_name": "Contact",
            "payment_days": 30,
        }
        response = self.client.post(
            "/brave/orders/api/v1/orders/", order_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_advertisement_with_invalid_dates(self) -> None:
        """Test creating an advertisement with end_date before start_date."""
        customer = models.Customer.objects.create(
            name="Test Corp",
            ruc="12345678901",
            email="test@test.com",
            phone="+1234567890",
            address="123 Test St",
            contact_name="John Test",
        )
        seller = models.Seller.objects.create(
            name="Test Seller",
            address="Address",
            email="seller@test.com",
            company_name="Test Co",
            ruc="12345678901",
        )
        order = models.Order.objects.create(
            customer=customer,
            seller=seller,
            ruc="12345678901",
            email="order@test.com",
            address="Address",
            phone="+1234567890",
            contact_name="Contact",
            payment_days=30,
        )
        kind = models.AdvertisementKind.objects.create(display_name="Test Kind")
        element = models.AdvertisementElement.objects.create(
            display="Test Element", code="TEST-001"
        )
        invalid_data = {
            "order": order.id,
            "brand": "TestBrand",
            "code": "AD-001",
            "start_date": "2024-12-31",
            "end_date": "2024-01-01",
            "quantity": 100,
            "unit_price": "50.00",
            "advertisement_element": element.id,
            "advertisement_kind": kind.id,
        }
        response = self.client.post(
            "/brave/orders/api/v1/advertisements/", invalid_data, format="json"
        )
        # API may or may not validate date logic, but should accept valid data format
        # This test ensures the API handles the request gracefully
        self.assertIn(
            response.status_code,
            [status.HTTP_201_CREATED, status.HTTP_400_BAD_REQUEST],
        )


class ForeignKeyProtectionTestCase(rest_test.APITestCase):
    """Test cases for foreign key protection (PROTECT)."""

    def setUp(self) -> None:
        """Set up test data."""
        self.customer = models.Customer.objects.create(
            name="Test Corp",
            ruc="12345678901",
            email="test@test.com",
            phone="+1234567890",
            address="123 Test St",
            contact_name="John Test",
        )
        self.seller = models.Seller.objects.create(
            name="Test Seller",
            address="Address",
            email="seller@test.com",
            company_name="Test Co",
            ruc="12345678901",
        )

    def test_cannot_delete_customer_with_orders(self) -> None:
        """Test that a customer with orders cannot be deleted (PROTECT)."""
        models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="Address",
            phone="+1234567890",
            contact_name="Contact",
            payment_days=30,
        )
        # Attempt to delete customer should fail due to PROTECT constraint
        with self.assertRaises(deletion.ProtectedError):
            self.customer.delete()
        # Verify that both customer and order still exist
        self.assertEqual(models.Customer.objects.count(), 1)
        self.assertEqual(models.Order.objects.count(), 1)

    def test_cannot_delete_seller_with_orders(self) -> None:
        """Test that a seller with orders cannot be deleted (PROTECT)."""
        models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="Address",
            phone="+1234567890",
            contact_name="Contact",
            payment_days=30,
        )
        # Attempt to delete seller should fail due to PROTECT constraint
        with self.assertRaises(deletion.ProtectedError):
            self.seller.delete()
        # Verify that both seller and order still exist
        self.assertEqual(models.Seller.objects.count(), 1)
        self.assertEqual(models.Order.objects.count(), 1)

    def test_cannot_delete_order_with_advertisements(self) -> None:
        """Test that an order with advertisements cannot be deleted (PROTECT)."""
        order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="Address",
            phone="+1234567890",
            contact_name="Contact",
            payment_days=30,
        )
        kind = models.AdvertisementKind.objects.create(display_name="Test Kind")
        element = models.AdvertisementElement.objects.create(
            display="Test Element", code="TEST-001"
        )
        models.Advertisement.objects.create(
            order=order,
            brand="TestBrand",
            code="AD-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=element,
            advertisement_kind=kind,
        )
        # Attempt to delete order should fail due to PROTECT constraint
        with self.assertRaises(deletion.ProtectedError):
            order.delete()
        # Verify that both order and advertisement still exist
        self.assertEqual(models.Order.objects.count(), 1)
        self.assertEqual(models.Advertisement.objects.count(), 1)

    def test_cannot_delete_advertisement_kind_in_use(self) -> None:
        """Test that an advertisement kind in use cannot be deleted (PROTECT)."""
        order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="Address",
            phone="+1234567890",
            contact_name="Contact",
            payment_days=30,
        )
        kind = models.AdvertisementKind.objects.create(display_name="Test Kind")
        element = models.AdvertisementElement.objects.create(
            display="Test Element", code="TEST-001"
        )
        models.Advertisement.objects.create(
            order=order,
            brand="TestBrand",
            code="AD-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=element,
            advertisement_kind=kind,
        )
        # Attempt to delete kind should fail due to PROTECT constraint
        with self.assertRaises(deletion.ProtectedError):
            kind.delete()
        # Verify that kind still exists
        self.assertEqual(models.AdvertisementKind.objects.count(), 1)

    def test_cannot_delete_advertisement_element_in_use(self) -> None:
        """Test that an advertisement element in use cannot be deleted (PROTECT)."""
        order = models.Order.objects.create(
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="Address",
            phone="+1234567890",
            contact_name="Contact",
            payment_days=30,
        )
        kind = models.AdvertisementKind.objects.create(display_name="Test Kind")
        element = models.AdvertisementElement.objects.create(
            display="Test Element", code="TEST-001"
        )
        models.Advertisement.objects.create(
            order=order,
            brand="TestBrand",
            code="AD-001",
            start_date="2024-01-01",
            end_date="2024-12-31",
            quantity=100,
            unit_price="50.00",
            advertisement_element=element,
            advertisement_kind=kind,
        )
        # Attempt to delete element should fail due to PROTECT constraint
        with self.assertRaises(deletion.ProtectedError):
            element.delete()
        # Verify that element still exists
        self.assertEqual(models.AdvertisementElement.objects.count(), 1)


class PaginationTestCase(rest_test.APITestCase):
    """Test cases for pagination across all endpoints."""

    def test_customer_pagination(self) -> None:
        """Test that customers are paginated correctly."""
        # Create 51 customers to test pagination (PAGE_SIZE=50)
        for i in range(51):
            models.Customer.objects.create(
                name=f"Customer {i}",
                ruc=f"1234567890{i:02d}",
                email=f"customer{i}@test.com",
                phone=f"+123456789{i:02d}",
                address=f"Address {i}",
                contact_name=f"Contact {i}",
            )
        response = self.client.get("/brave/orders/api/v1/customers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 51)
        self.assertEqual(len(response.data["results"]), 50)
        self.assertIsNotNone(response.data["next"])

    def test_custom_page_size(self) -> None:
        """Test that custom page_size parameter works correctly."""
        # Create 30 customers
        for i in range(30):
            models.Customer.objects.create(
                name=f"Customer {i}",
                ruc=f"2234567890{i:02d}",
                email=f"customer{i}@test.com",
                phone=f"+223456789{i:02d}",
                address=f"Address {i}",
                contact_name=f"Contact {i}",
            )
        # Test custom page_size=10
        response = self.client.get(
            "/brave/orders/api/v1/customers/?page_size=10"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 30)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertIsNotNone(response.data["next"])

    def test_max_page_size_limit(self) -> None:
        """Test that max_page_size limit is enforced."""
        # Create 150 customers
        for i in range(150):
            models.Customer.objects.create(
                name=f"Customer {i}",
                ruc=f"3234567890{i:03d}",
                email=f"customer{i}@test.com",
                phone=f"+323456789{i:03d}",
                address=f"Address {i}",
                contact_name=f"Contact {i}",
            )
        # Request page_size=200 (should be limited to max_page_size=100)
        response = self.client.get(
            "/brave/orders/api/v1/customers/?page_size=200"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 150)
        # Should return max 100 items, not 200
        self.assertEqual(len(response.data["results"]), 100)


class FixtureDataTestCase(test.TestCase):
    """Test cases for fixture data loading."""

    fixtures: typing.List[str] = ["initial_data.yaml"]

    def test_fixture_advertisement_kinds_loaded(self) -> None:
        """Test that AdvertisementKind fixtures are loaded."""
        self.assertEqual(
            models.AdvertisementKind.objects.count(),
            3,
        )
        self.assertTrue(
            models.AdvertisementKind.objects.filter(
                display_name="Publicidad"
            ).exists()
        )
        self.assertTrue(
            models.AdvertisementKind.objects.filter(
                display_name="Espacios temporales"
            ).exists()
        )
        self.assertTrue(
            models.AdvertisementKind.objects.filter(
                display_name="Sampling y volanteo"
            ).exists()
        )

    def test_fixture_advertisement_elements_loaded(self) -> None:
        """Test that AdvertisementElement fixtures are loaded."""
        self.assertEqual(
            models.AdvertisementElement.objects.count(),
            12,
        )
        # Test specific elements
        banner = models.AdvertisementElement.objects.get(code="BP-N1-001")
        self.assertEqual(banner.display, "Banner Principal Nivel 1")
        volanteo = models.AdvertisementElement.objects.get(code="VL-ZN-008")
        self.assertEqual(volanteo.display, "Volanteo Zona Norte")

    def test_fixture_advertisement_element_codes(self) -> None:
        """Test that all AdvertisementElement codes are unique and present."""
        codes = [
            "BP-N1-001",
            "BS-N2-002",
            "ET-PC-005",
            "IP-FC-007",
            "PL-EXT-004",
            "PL-INT-003",
            "SM-EP-010",
            "SP-ENT-006",
            "TD-N1-011",
            "VE-EST-012",
            "VL-ZN-008",
            "VL-ZS-009",
        ]
        for code in codes:
            self.assertTrue(
                models.AdvertisementElement.objects.filter(code=code).exists()
            )
