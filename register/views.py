from django.shortcuts import render

# Create your views here.

def register(requests):
    return render(requests,'register/register.html')