"""Models for the quotes app."""

from django.db import models


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.text
