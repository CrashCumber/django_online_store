from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from goods.models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver





@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Basket(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_date = models.DateTimeField(default=timezone.now)
    number = models.IntegerField()

    def __str__(self):
        return f"Basket item {self.product} of {self.user}"


