from django.contrib import admin
from .models import User, Basket

admin.site.unregister(User)


class MembershipInline(admin.TabularInline):
    model = Basket


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', )
    inlines = (MembershipInline,)
