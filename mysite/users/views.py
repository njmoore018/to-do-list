from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from home import views as v

# Create your views here.
def register(response):
    if response.method == "POST":
        form = UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            v.create(response)
            return redirect("login/")
    else:
        form = UserCreationForm

    return render(response, "users/register.html", {"form":form})
