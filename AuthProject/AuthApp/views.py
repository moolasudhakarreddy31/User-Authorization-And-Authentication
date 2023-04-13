from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):

    return render(request,'AuthApp/home.html')



@login_required
def java_view(request):

    return render(request,'AuthApp/java.html')


def python_view(request):

    return render(request,'AuthApp/python.html')


def aptitude_view(request):

    return render(request,'AuthApp/aptitude.html')





