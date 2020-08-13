from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from goods.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('\n\n\nreceived\n\n\n')
    if created:
        Basket.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.basket.save()


class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}`s basket"


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=timezone.now)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Basket item {self.product} "





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
