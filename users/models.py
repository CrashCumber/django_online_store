from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

from goods.models import Product


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL)
#     # product = models.ManyToManyField(Product, blank=True, null=True)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100, unique=True, blank=True, null=True)
#     password = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=timezone.now)
    number = models.IntegerField()

    def __str__(self):
        return f"Basket item {self.product} of {self.user}"
