from django.contrib import admin
from .models import Basket, BasketItem


class MembershipInline(admin.TabularInline):
    model = BasketItem


@admin.register(Basket)
class UserAdminM(admin.ModelAdmin):
    inlines = (MembershipInline,)


