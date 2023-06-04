from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def register_user(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("automobiles:home")
    context = {"form": form}
    return render(request, "registration/register_user.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("automobiles:home")
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again"))
            return redirect("users:logins")
    else:
        return render(request, 'authenticate/login.html', {})


def delete_user(request):
    return render(request, "delete/remove_user.html")

# def delete_user(request, username):
#     context = {}
#
#     if not request.user.is_authenticated:
#         return redirect("registration/register.html")
#
#     if request.method == 'DELETE':
#         try:
#             user = request.user
#             user.delete('Niraj')
#             context['msg'] = 'Bye Bye'
#         except Exception as e:
#             context['msg'] = 'Something went wrong!'
#
#     else:
#         context['msg'] = 'Request method should be "DELETE"!'
#
#     return render(request, 'delete/remove_user.html', context=context)


# from django.contrib.auth.models import User
# user = User.objects.create_user(username='Niraj',
#                                  email='deyneeraj666.com',
#                                  password='glass onion')
