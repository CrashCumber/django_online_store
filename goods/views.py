from django.http import HttpResponse
from django.shortcuts import render, redirect
from goods.forms import ProductForm
from goods.models import Product, Banner
from users.models import User, Basket, BasketItem


def main(request):
    if request.method == 'GET':
        products = Product.objects.all()
        banners = Banner.objects.all()
        return render(request, 'main.html', {'products': products, 'banners': banners})
    else:
        return HttpResponse(status=405)


def product(request, product_id):
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
