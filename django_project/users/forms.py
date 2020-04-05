from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        """
        This class is to contain our forms configuration, for some reason unknown.
        TODO: clarify the Meta class usage in UserRegisterForm - why the hell is that the way to go?
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']