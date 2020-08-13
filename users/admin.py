from django.contrib import admin
from .models import Basket, BasketItem


class MembershipInline(admin.TabularInline):
    model = BasketItem


@admin.register(Basket)
class UserAdmin(admin.ModelAdmin):
    # list_display = ('username',)#, 'email','password' )
    inlines = (MembershipInline,)




# @admin.register(Basket)
# class BasketAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product')
#     filter_horizonta = ['user']
#     # search_fields = []
