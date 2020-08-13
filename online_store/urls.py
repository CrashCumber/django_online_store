from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views
from goods import views as goods_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', users_views.register, name='register'),
    path('basket/', users_views.user_basket, name='basket'),
    path('products/<int:product_id>/', goods_views.product, name='product'),
    path('products/<int:product_id>/delete/', goods_views.product_delete, name='product_delete'),
    path('', goods_views.main, name='main'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
