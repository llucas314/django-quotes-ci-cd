"""Serializers for the quotes app."""

from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            "id",
            "text",
            "author",
        )
