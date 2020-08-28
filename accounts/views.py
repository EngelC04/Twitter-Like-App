from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# Create your views here.
#Function based views to Class Based Views

def login_view(request,*args, **kwargs):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user_= form.get_user()
        login(request, user_)
        return redirect("/")
    context = {
        "form" : form,
        "btn_label" : "Login",
        "title" : "Login"
    }
    return render(request, "accounts/auth.html",context)

def logout_view(request, *args, **kwargs):
    if request.method == "POST":
        logout(request)
        return redirect("/login")
    context = {
        "form": None,
        "btn_label": "Click to confirm",
        "title" : "Logout"
    }
    return render(request, "accounts/auth.html",context) 

def register_view(request,*args, **kwargs):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=True)
        user.set_password(form.cleaned_data.get("password1"))
        login(request,user)
        return redirect("/")
        #print(form.cleaned_data)
        #print (form.cleaned_data)
        #username = form.cleaned_data.get("username")               
    context = {
        "form":form,
        "btn_label":"Register",
        "title": "Register"
    }
    return render(request, "accounts/auth.html",context)
