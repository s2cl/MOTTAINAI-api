from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django_boost.models.mixins import UUIDModelMixin, TimeStampModelMixin
from datetime import timedelta


# Create your models here.

class User(AbstractUser):
    limit_num = models.DurationField(default=timedelta(days=3))

