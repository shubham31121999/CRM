from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput,TextInput


# - Registering or creation of  a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username','password1','password2']  #passsword1 is orgianal password while password2 is just confirming password1.

# - Login a User
        
class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())       
