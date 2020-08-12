from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from goods.forms import ProductForm
from goods.models import Product, Banner
from users.models import User, Basket, Profile


def main(request):
    if request.method == 'GET':
        products = Product.objects.all()
        banners = Banner.objects.all()
        return render(request, 'main.html', {'products': products, 'banners': banners})


def product(request, product_id):
    form = ProductForm()

    if request.method == 'GET':
        item = Product.objects.filter(id=product_id).first()
        return render(request, 'item.html', {'item': item, 'item_form': form})

    if request.method == 'POST':
        form = ProductForm(request.POST)
        item = Product.objects.filter(id=product_id).first()

        if request.user.is_authenticated:
            user_id = request.session.get('_auth_user_id')
            # user = User.objects.get(pk=user_id)
            user = User.objects.get(pk=user_id)
            profile = Profile.objects.filter(user=user).first()

            basket_item = Basket.objects.filter(user=profile, product=item).first()
            if basket_item is None:
                number = int(form.data["number"])
                Basket.objects.create(user=profile, product=item, number=number)
            else:
                basket_item.number += int(form.data["number"])
                basket_item.save()

            return redirect('/basket/')
        else:
            return redirect('/login/')


    # if request.method == 'DELETE':
    #
    #     user_id = request.session['user_id']
    #     user = User.objects.get(pk=user_id)
    #     item = Product.objects.filter(id=product_id).first()
    #
    #     item = Basket.objects.filter(user=user, product=item).first()
    #     item.delete()

    # if request.method == 'PUT':
    #
    #     user_id = request.session['user_id']
    #     user = User.objects.get(pk=user_id)
    #     item = Product.objects.filter(id=product_id).first()
    #
    #     item = Basket.objects.filter(user=user, product=item).first()
        # item.delete()
