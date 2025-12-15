"""Tests for the brave_orders application."""

import typing

import django.test as test  # pylint: disable=consider-using-from-import
import rest_framework.status as status  # pylint: disable=consider-using-from-import
import rest_framework.test as rest_test  # pylint: disable=consider-using-from-import

import brave_orders.models as models  # pylint: disable=consider-using-from-import


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
        self.assertEqual(
            models.Customer.objects.count(), 1  # pylint: disable=no-member
        )
        self.assertEqual(
            models.Customer.objects.get().name,
            "Test Corp",  # pylint: disable=no-member
        )

    def test_list_customers(self) -> None:
        """Test listing customers via GET request."""
        models.Customer.objects.create(  # pylint: disable=no-member
            **self.customer_data
        )
        response = self.client.get("/brave/orders/api/v1/customers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(len(response.data["results"]), 1)

    def test_retrieve_customer(self) -> None:
        """Test retrieving a specific customer via GET request."""
        customer = models.Customer.objects.create(  # pylint: disable=no-member
            **self.customer_data
        )
        response = self.client.get(
            f"/brave/orders/api/v1/customers/{customer.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Test Corp")
        self.assertEqual(response.data["ruc"], "12345678901")

    def test_update_customer(self) -> None:
        """Test updating a customer via PUT request."""
        customer = models.Customer.objects.create(  # pylint: disable=no-member
            **self.customer_data
        )
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
        customer = models.Customer.objects.create(  # pylint: disable=no-member
            **self.customer_data
        )
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
        customer = models.Customer.objects.create(  # pylint: disable=no-member
            **self.customer_data
        )
        response = self.client.delete(
            f"/brave/orders/api/v1/customers/{customer.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            models.Customer.objects.count(), 0  # pylint: disable=no-member
        )


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
        self.assertEqual(
            models.Seller.objects.count(), 1  # pylint: disable=no-member
        )

    def test_list_sellers(self) -> None:
        """Test listing sellers via GET request."""
        models.Seller.objects.create(  # pylint: disable=no-member
            **self.seller_data
        )
        response = self.client.get("/brave/orders/api/v1/sellers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)


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
            1,  # pylint: disable=no-member
        )

    def test_list_advertisement_kinds(self) -> None:
        """Test listing advertisement kinds via GET request."""
        models.AdvertisementKind.objects.create(  # pylint: disable=no-member
            **self.kind_data
        )
        response = self.client.get("/brave/orders/api/v1/advertisement-kinds/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)


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
            models.AdvertisementElement.objects.count(),  # pylint: disable=no-member
            1,
        )
        self.assertEqual(
            models.AdvertisementElement.objects.get().code,  # pylint: disable=no-member
            "TEST-001",
        )

    def test_list_advertisement_elements(self) -> None:
        """Test listing advertisement elements via GET request."""
        models.AdvertisementElement.objects.create(  # pylint: disable=no-member
            **self.element_data
        )
        response = self.client.get(
            "/brave/orders/api/v1/advertisement-elements/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["code"], "TEST-001")

    def test_retrieve_advertisement_element(self) -> None:
        """Test retrieving a specific advertisement element via GET request."""
        element = models.AdvertisementElement.objects.create(  # pylint: disable=no-member
            **self.element_data
        )
        response = self.client.get(
            f"/brave/orders/api/v1/advertisement-elements/{element.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["display"], "Test Banner")
        self.assertEqual(response.data["code"], "TEST-001")


class AdvertisementViewSetTestCase(rest_test.APITestCase):
    """Test cases for Advertisement CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.customer = (
            models.Customer.objects.create(  # pylint: disable=no-member
                name="Test Corp",
                ruc="12345678901",
                email="test@testcorp.com",
                phone="+1234567890",
                address="123 Test St",
                contact_name="John Test",
            )
        )
        self.seller = models.Seller.objects.create(  # pylint: disable=no-member
            name="Jane Seller",
            address="456 Seller Ave",
            email="jane@seller.com",
            company_name="Seller Solutions Inc",
            ruc="98765432109",
        )
        self.order = models.Order.objects.create(  # pylint: disable=no-member
            customer=self.customer,
            seller=self.seller,
            ruc="12345678901",
            email="order@test.com",
            address="123 Order St",
            phone="+1234567890",
            contact_name="Jane Order",
            payment_days=30,
        )
        self.kind = models.AdvertisementKind.objects.create(  # pylint: disable=no-member
            display_name="Test Kind"
        )
        self.element = models.AdvertisementElement.objects.create(  # pylint: disable=no-member
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
        self.assertEqual(
            models.Advertisement.objects.count(), 1  # pylint: disable=no-member
        )

    def test_list_advertisements(self) -> None:
        """Test listing advertisements via GET request."""
        models.Advertisement.objects.create(  # pylint: disable=no-member
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


class OrderViewSetTestCase(rest_test.APITestCase):
    """Test cases for Order CRUD operations via REST API."""

    def setUp(self) -> None:
        """Set up test data."""
        self.customer = (
            models.Customer.objects.create(  # pylint: disable=no-member
                name="Test Corp",
                ruc="12345678901",
                email="test@testcorp.com",
                phone="+1234567890",
                address="123 Test St",
                contact_name="John Test",
            )
        )
        self.seller = models.Seller.objects.create(  # pylint: disable=no-member
            name="Jane Seller",
            address="456 Seller Ave",
            email="jane@seller.com",
            company_name="Seller Solutions Inc",
            ruc="98765432109",
        )
        self.kind = models.AdvertisementKind.objects.create(  # pylint: disable=no-member
            display_name="Test Kind"
        )
        self.element = models.AdvertisementElement.objects.create(  # pylint: disable=no-member
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
        self.assertEqual(
            models.Order.objects.count(), 1  # pylint: disable=no-member
        )
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
        self.assertEqual(
            models.Order.objects.count(), 1  # pylint: disable=no-member
        )
        self.assertEqual(
            models.Advertisement.objects.count(), 1  # pylint: disable=no-member
        )
        self.assertEqual(len(response.data["advertisements"]), 1)
        self.assertEqual(
            response.data["advertisements"][0]["brand"], "TestBrand"
        )

    def test_list_orders(self) -> None:
        """Test listing orders via GET request."""
        models.Order.objects.create(  # pylint: disable=no-member
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
        order = models.Order.objects.create(  # pylint: disable=no-member
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
        order = models.Order.objects.create(  # pylint: disable=no-member
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
        models.Advertisement.objects.create(  # pylint: disable=no-member
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
        self.assertEqual(
            models.Advertisement.objects.count(), 1  # pylint: disable=no-member
        )
        self.assertEqual(
            models.Advertisement.objects.get().brand,  # pylint: disable=no-member
            "NewBrand",
        )

    def test_partial_update_order(self) -> None:
        """Test partially updating an order via PATCH request."""
        order = models.Order.objects.create(  # pylint: disable=no-member
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


class PaginationTestCase(rest_test.APITestCase):
    """Test cases for pagination across all endpoints."""

    def test_customer_pagination(self) -> None:
        """Test that customers are paginated correctly."""
        # Create 51 customers to test pagination (PAGE_SIZE=50)
        for i in range(51):
            models.Customer.objects.create(  # pylint: disable=no-member
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


class FixtureDataTestCase(test.TestCase):
    """Test cases for fixture data loading."""

    fixtures: typing.List[str] = ["initial_data.yaml"]

    def test_fixture_advertisement_kinds_loaded(self) -> None:
        """Test that AdvertisementKind fixtures are loaded."""
        self.assertEqual(
            models.AdvertisementKind.objects.count(),
            3,  # pylint: disable=no-member
        )
        self.assertTrue(
            models.AdvertisementKind.objects.filter(  # pylint: disable=no-member
                display_name="Publicidad"
            ).exists()
        )
        self.assertTrue(
            models.AdvertisementKind.objects.filter(  # pylint: disable=no-member
                display_name="Espacios temporales"
            ).exists()
        )
        self.assertTrue(
            models.AdvertisementKind.objects.filter(  # pylint: disable=no-member
                display_name="Sampling y volanteo"
            ).exists()
        )

    def test_fixture_advertisement_elements_loaded(self) -> None:
        """Test that AdvertisementElement fixtures are loaded."""
        self.assertEqual(
            models.AdvertisementElement.objects.count(),
            12,  # pylint: disable=no-member
        )
        # Test specific elements
        banner = models.AdvertisementElement.objects.get(  # pylint: disable=no-member
            code="BP-N1-001"
        )
        self.assertEqual(banner.display, "Banner Principal Nivel 1")
        volanteo = models.AdvertisementElement.objects.get(  # pylint: disable=no-member
            code="VL-ZN-008"
        )
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
                models.AdvertisementElement.objects.filter(  # pylint: disable=no-member
                    code=code
                ).exists()
            )
