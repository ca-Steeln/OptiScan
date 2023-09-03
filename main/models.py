from django.db import models
from .settings import SEARCH_TYPE_CHOICES, DEFAULT_SEARCH_TYPE, SEARCH_BEHAVIOR_CHOICES, DEFAULT_SEARCH_BEHAVIOR

# Create your models here.

class Filter(models.Model):

    slug = models.SlugField(unique=False, blank=False, null=True)
    key_word = models.CharField(max_length=10_000, blank=False)
    content = models.TextField(max_length=10_000, blank=False)
    case = models.BooleanField(default=True , blank=True, null=False)
    search_type = models.CharField(max_length=128, choices=SEARCH_TYPE_CHOICES, default=DEFAULT_SEARCH_TYPE, blank=False, null=True)
    search_behavior = models.CharField(max_length=128, choices=SEARCH_BEHAVIOR_CHOICES, default=DEFAULT_SEARCH_BEHAVIOR, blank=False, null=True)
    num_keys = models.DecimalField(max_digits=10_000, decimal_places=0, blank=True, null=True)


