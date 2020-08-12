from django.contrib import admin
from goods.models import Product
from .models import User, Basket

# admin.site.unregister(User)



class MembershipInline(admin.TabularInline):
    pass


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    filter_horizonta = ['user']
    # search_fields = []

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email','password' )
#     inlines = (MembershipInline,)
