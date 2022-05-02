from django.shortcuts import render, redirect, HttpResponse
from .forms import UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.
""" Authentication Views """

#function based views:

def login_view(request):
    if request.method == 'POST':
        usern = request.POST.get('username')
        #username taken from the form input with the ---name=username---! 
        password = request.POST.get('password')
        #password taken from the form input with the ---name=password---! 
        user = authenticate(username=usern, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome, {user.username}!' ) 
            return redirect('home')
        else:
            return HttpResponse('<h3>Something is wrong! Try again, please...</h3>')
    return render(request, 'login.html')


def register_view(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can sign in.')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    
    return render(request, 'register.html', {'form' : form})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, 'You logged out successfully!')

        return redirect('login')

    return render(request, 'logout.html')




