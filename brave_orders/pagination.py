"""Pagination classes for the brave_orders application."""

import typing

import rest_framework.pagination as pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    """Standard pagination class for API responses.

    This pagination class provides consistent pagination across all API endpoints
    with a default page size of 50 items per page. Clients can override the page
    size using the 'page_size' query parameter up to a maximum of 100 items.

    Attributes:
        page_size (int): The default number of items to include on a page.
            Default is 50.
        page_size_query_param (str): The name of the query parameter that allows
            clients to specify a custom page size. Default is 'page_size'.
        max_page_size (int): The maximum page size that clients can request.
            Default is 100.

    Example:
        # Default pagination (50 items per page)
        GET /api/v1/customers/

        # Custom page size (20 items per page)
        GET /api/v1/customers/?page_size=20

        # Navigate to page 2
        GET /api/v1/customers/?page=2

        # Combine page and page_size
        GET /api/v1/customers/?page=2&page_size=30

    Response Format:
        {
            "count": 150,
            "next": "http://localhost:8000/api/v1/customers/?page=2",
            "previous": null,
            "results": [...]
        }
    """

    page_size: int = 50
    page_size_query_param: typing.Optional[str] = "page_size"
    max_page_size: int = 100
