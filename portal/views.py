from django.shortcuts import render


def index(request):
    return render(request, 'portal/base.html')

def login(request):
    return render(request, 'portal/login.html')

def dashboard(request):
    return render(request, 'portal/dashboard.html')