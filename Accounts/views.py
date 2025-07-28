from django.shortcuts import render,redirect
from Accounts.forms import SignUpForm,LoginForm
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def create_account(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
  
        if form.is_valid():

            form.save()
            return redirect('login')
          
    else:
        form = SignUpForm()
    
    return render(request, 'Users/signup.html', {'form': form})

def user_login(request):
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
           
            return redirect('post')
        else:
            messages.error(request,'invalid username or password')

    else:
        form=LoginForm()
    return render(request,'Users/login1.html',{'form':form})

def custom_logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out due to inactivity.")
    return redirect('login') 

@login_required
def user_profile(request):
    if user.is_authenticated:
        user= request.user
        return render(request, 'Users/profile.html', {'user': user})
   







# Create your views here.
