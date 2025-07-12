"""Views for the quotes app."""

import random

from rest_framework import generics, status, views
from rest_framework.response import Response

from .models import Quote
from .serializers import QuoteSerializer


class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class RandomQuoteAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        quotes = Quote.objects.all()
        if quotes:
            random_quote = random.choice(quotes)
            serializer = QuoteSerializer(random_quote)
            return Response(serializer.data)
        return Response(
            {"detail": "No quote available"}, status=status.HTTP_404_NOT_FOUND
        )
