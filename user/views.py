from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


def register(request):
    status = request.GET.get('status')
    return render(request, 'register.html', {'status': status})


def login(request):
    return HttpResponse('You are in the login page')


def home(request):
    return HttpResponse('You are in the user home')


def save(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    age = request.POST.get('age')
    try:
        user = User(
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        user.save()
        return redirect('/user/register?status=1')
    except:
        return redirect('/user/register?status=2')

