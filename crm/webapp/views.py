from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import CreateUserForm, LoginForm

def home(request):
    return render(request, 'webapp/index.html')



# --> Register page


def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('login')
    

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)


# - Login form of user

def user_login(request):

    form = LoginForm

    if request.method =="POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username,password=password)

            if user is not None:
                auth.login(request, user)

    context = {'form1':form}

    return render(request, 'webapp/login.html',context=context)

# - Dashboard view











# - User logout

def user_logout(request):
    auth.logout(request)

    return redirect("login")
