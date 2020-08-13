from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class UserRegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Это поле обязательно')

    class Meta:
        model = User
        fields = ('username',)
