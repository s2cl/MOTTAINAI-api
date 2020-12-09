from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django_boost.models.mixins import UUIDModelMixin, TimeStampModelMixin
from datetime import timedelta


# Create your models here.

class User(AbstractUser):
    limit_num = models.DurationField(default=timedelta(days=3))

class MasterItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='masteritems')
    image = models.URLField(blank=True, default='') #Django storage  https://django-storages.readthedocs.io/en/latest/
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=30, blank=True, default='')
    def __str__(self):
        return self.name

class Item(models.Model):
    place = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    limit = models.DateField(null=True)
    count = models.IntegerField()
    master = models.ForeignKey(MasterItem, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.user.places.filter(name=self.place).count() == 0:
            Place.objects.create(name=self.place, user=self.user)

class ShoppingList(UUIDModelMixin, TimeStampModelMixin):
    """買い物リスト"""
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, models.CASCADE, related_name='shoppinglists')
    option = models.IntegerField()
    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    """買い物リストの食品"""
    shoppinglist = models.ForeignKey(ShoppingList, models.CASCADE, related_name='shoppingitems')
    master = models.ForeignKey(MasterItem, models.CASCADE)
    num = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)])

class Place(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='places')
    class Meta:
        unique_together = ('name', 'user')
    def __str__(self):
        return self.name
