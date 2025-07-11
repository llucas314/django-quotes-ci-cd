from django.urls import path
from .views import QuoteAPIView, RandomQuoteAPIView

urlpatterns = [
    path("", QuoteAPIView.as_view(), name="quote-list"),
    path("random/", RandomQuoteAPIView.as_view(), name="random-quote"),
]
