from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegisterUserForm


def register_user(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    if request.method != "POST":
        # form = UserCreationForm()
        form = RegisterUserForm()
    else:
        form = RegisterUserForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            messages.success(request, 'Register Successfully!')
            return redirect("automobiles:home")
    context = {"form": form, "current_year": current_year, 'time': time}
    return render(request, "registration/register_user.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("automobiles:home")
        messages.success(request, 'There Was An Error Logging In, Try Again!')
        return redirect("users:logins")
    return render(request, 'authenticate/login.html')


def delete_user(request):
    now = datetime.now()
    current_year = now.year
    time = now.strftime('%H:%M:%S')
    context = {"current_year": current_year, 'time': time}
    return render(request, "delete/remove_user.html", context)
