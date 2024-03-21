from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from .models import ClientRecord

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


# - Add record form
    
class CreaterecordForm(forms.ModelForm):
    class Meta:

        model = ClientRecord
        fields = ['first_name','last_name','email','phone','address','city','state','country']


# - Update record Form
        
class UpdateRecordForm(forms.ModelForm):
    class Meta:

        model = ClientRecord
        fields = ['first_name','last_name','email','phone','address','city','state','country']