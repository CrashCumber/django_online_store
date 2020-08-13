from django.contrib.auth.models import User, Group
from django.core.signals import request_finished
from django.utils import timezone
from django.db import models
from goods.models import Product
from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user_basket(sender, instance, created, **kwargs):
    if created:
        Basket.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.basket.save()

    group = Group.objects.get(name='managers')
    if group in instance.groups.all():
        instance.groups.add(group)
        User.objects.filter(id=instance.id).update(is_staff=True)
    else:
        User.objects.filter(id=instance.id).update(is_staff=False)



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

