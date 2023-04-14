from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AuthApp.forms import SignUpForm
from django.http import HttpResponseRedirect


# Create your views here.

def home_view(request):

    return render(request,'AuthApp/home.html')



@login_required
def java_view(request):

    return render(request,'AuthApp/java.html')

@login_required

def python_view(request):

    return render(request,'AuthApp/python.html')

@login_required
def aptitude_view(request):

    return render(request,'AuthApp/aptitude.html')


def logout_view(request):

    return render(request,'AuthApp/logout.html')

def signupform_view(request):
    form=SignUpForm()
    if request.method=='POST':
            form=SignUpForm(request.POST)
            # if form.is_valid():
            #      form.save()
            # user=form.save()                    # Below Three lines are User Authenatination
            # user.set_password(user.password)
            # user.save()


            return HttpResponseRedirect('accounts/login')
    return render(request,'AuthApp/signup.html',{'form':form})
