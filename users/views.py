from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .forms import CustomUserCreationForm

# Create your views here.

""" this is the sign-up/registration view """
def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
            messages.success(request, 'Account created succesfully!!')
        else:
            messages.error(request, 'Sorry, an error has occured during registration.')


    context = {'form': form}
    return render(request, 'users/sign-up.html', context)


""" the login view """
def loginUser(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Sorry username or password is incorrect.')

    return render(request, 'users/login.html')


""" the logout view """
def logoutUser(request):
    logout(request)
    return redirect('login')


""" this is the homepage view only logged in users can view"""
@login_required(login_url = 'login')
def homePage(request):

    return render(request, 'users/home.html')