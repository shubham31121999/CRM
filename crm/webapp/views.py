from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import CreateUserForm, LoginForm,CreaterecordForm,UpdaterecordForm


from .models import ClientRecord
from django.contrib.auth.decorators import login_required


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
    

    context = {'form1':form}

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

                return redirect("dashboard")

    context = {'form1':form}

    return render(request, 'webapp/login.html',context=context)

# - Dashboard view

@login_required(login_url='login')
def dashboard(request):


    user_records = ClientRecord.objects.all()
    
    context = {'clientrecord':user_records}

    
    return render(request, 'webapp/dashboard.html',context=context)

# - Add a record

@login_required(login_url='login')
def create_record(request):
    form = CreaterecordForm()

    if request.method == "POST":
        form = CreaterecordForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request,'webapp/create.html',context=context)










# - User logout

def user_logout(request):
    auth.logout(request)

    return redirect("login")
