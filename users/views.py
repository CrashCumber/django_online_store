from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from users.models import User, Basket, BasketItem


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():

            user = user_form.save()
            login(request, user)

            return redirect('/')
        else:
            # print(user_form.error_messages)
            user_form = UserRegistrationForm()
            return render(request, 'registration/register.html', {'user_form': user_form})

    elif request.method == 'GET':
        user_form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'user_form': user_form})
    else:
        return HttpResponse(status=405)


@login_required
def user_basket(request):
    if request.method == 'GET':

        user_id = request.session['_auth_user_id']
        user = User.objects.get(pk=user_id)

        basket = Basket.objects.filter(user=user).first()
        basket_items = BasketItem.objects.filter(basket=basket).all()

        return render(request, 'basket.html', {'basket_items': basket_items})

