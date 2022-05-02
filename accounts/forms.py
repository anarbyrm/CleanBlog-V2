from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#----Registration form will be used in views----
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']



        