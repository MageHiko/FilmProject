from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.http import Http404
from django.views.generic import View

class SignupView(View):
    def get(self, request, *args, **kvargs):
        if request.user.is_authenticated:
            raise Http404
        return render(request, "signup.html")
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username = username,
                password = password
            )
        else:
            messages.info(request, "This username already exist")
        return redirect ("signup")
        
class LoginUserViews(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            raise Http404
        return render(request, "login.html")
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
        else:
            messages.info(request, "This username is not exist")
        
        return redirect ("index")

class LogoutViews(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect ("login")
