"""Tests for the quotes app."""

from django.urls import reverse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase

from .models import Quote
from .serializers import QuoteSerializer


class QuoteAPITestCase(APITestCase):
    def setUp(self):
        self.quote1 = Quote.objects.create(
            text="Code is poetry.",
            author="Programmer A",
        )
        self.quote2 = Quote.objects.create(
            text="Debugging is like being a detective.",
            author="Programmer B",
        )
        self.url = reverse("quote-list")

    def test_get_all_quotes(self):
        """
        Ensure we can retrieve a list of all quotes.
        """
        response = self.client.get(self.url)
        if isinstance(response, Response):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            # Check if the response data matches the data of all quotes
            quotes = Quote.objects.all()
            serializer = QuoteSerializer(quotes, many=True)
            self.assertEqual(response.data, serializer.data)
            if response.data is not None:
                self.assertEqual(len(response.data), 2)  # Check count

    def test_get_quotes_empty_db(self):
        """
        Ensure an empty list is returned when no quotes exist.
        """
        Quote.objects.all().delete()  # Clear existing quotes
        response = self.client.get(self.url)
        if isinstance(response, Response):
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, [])


class RandomQuoteAPITestCase(APITestCase):
    def setUp(self):
        self.quote1 = Quote.objects.create(text="Hello world.", author="Coder C")
        self.quote2 = Quote.objects.create(
            text="Keep calm and code on.", author="Coder D"
        )
        self.quote3 = Quote.objects.create(
            text="Eat, sleep, code, repeat.", author="Coder E"
        )
        self.url = reverse("random-quote")

    def test_get_random_quote_success(self):
        """
        Ensure we can retrieve a single random quote when quotes exist.
        """
        response = self.client.get(self.url)
        if isinstance(response, Response) and response.data is not None:
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            # Verify that the returned quote's data matches
            returned_text = response.data["text"]
            returned_author = response.data["author"]

            all_quotes = Quote.objects.all()
            # Check if the returned quote matches one of the existing quotes
            self.assertTrue(
                any(
                    q.text == returned_text and q.author == returned_author
                    for q in all_quotes
                )
            )

            # Check if it's a single object, not a list
            self.assertIsInstance(response.data, dict)
            self.assertIn("id", response.data)
            self.assertIn("text", response.data)
            self.assertIn("author", response.data)

    def test_get_random_quote_empty_db(self):
        """
        Ensure 404 Not Found is returned when no quotes exist.
        """
        Quote.objects.all().delete()  # Clear existing quotes
        response = self.client.get(self.url)
        if isinstance(response, Response):
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
            self.assertEqual(response.data, {"detail": "No quote available"})
