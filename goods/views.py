from django.http import HttpResponse
from django.shortcuts import render, redirect
from goods.forms import ProductForm
from goods.models import Product, Banner
from users.models import User, Basket, BasketItem


def main(request):
    """Main page endpoint.
    :param request
    :return: main page with banners and products.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        banners = Banner.objects.all()
        return render(request, 'main.html', {'products': products, 'banners': banners})
    else:
        return HttpResponse(status=405)


def product(request, product_id):
    """ Product endpoint with information and ability to buy.
    :param request:
    :param product_id: id product from Product model.
    :return: for GET - product information page
             for POST - save product in user basket and redirect to basket.
    """
    product = Product.objects.filter(id=product_id).first()

    if request.method == 'GET':
        quantity_form = ProductForm()
        return render(request, 'product.html', {'product': product, 'quantity_form': quantity_form})

    elif request.method == 'POST':
        quantity_form = ProductForm(request.POST)

        if not quantity_form.is_valid():
            return HttpResponse(status=404)

        quantity = quantity_form.cleaned_data["quantity"]

        if request.user.is_authenticated:
            user_id = request.session.get('_auth_user_id')
            user = User.objects.get(pk=user_id)

            basket = Basket.objects.filter(user=user).first()
            basket_item = BasketItem.objects.filter(basket=basket, product=product).first()

            if basket_item is None:
                BasketItem.objects.create(basket=basket, product=product, quantity=int(quantity))
            else:
                basket_item.quantity += int(quantity)
                basket_item.save()

            return redirect('/basket/')
        else:
            return redirect('/login/')
    else:
        return HttpResponse(status=405)


def product_delete(request, product_id):
    """Delete product endpoint.
    :param request
    :param product_id: id for product
    :return: for auth user - delete product from user basket and redirect to basket.
             for not auth user - redirect to login.
    """
    if request.method == 'GET':
        product = Product.objects.filter(id=product_id).first()

        if request.user.is_authenticated:
            user_id = request.session.get('_auth_user_id')
            user = User.objects.get(pk=user_id)

            basket = Basket.objects.filter(user=user).first()
            basket_item = BasketItem.objects.filter(basket=basket, product=product).first()

            basket_item.delete()

            return redirect('/basket/')
        else:
            return redirect('/login/')
    else:
        return HttpResponse(status=405)
