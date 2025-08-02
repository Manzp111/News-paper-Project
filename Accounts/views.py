from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from allauth.account.views import LoginView

from .models import CustomUser
from Accounts.forms import SignUpForm,LoginForm

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
            if request.user.role == 'admin':
                return redirect('admin')
            elif request.user.role in ['author','supervisor']:
                return redirect('worker_dashboard')
            else:
                return redirect('post')
            
           
        else:
            messages.error(request,'invalid username or password')

    else:
        form=LoginForm()
    return render(request,'Users/login1.html',{'form':form})

class CustomLoginView(LoginView):
    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'admin':
                return '/admin/dashboard/'  # Change to your admin dashboard URL
            elif user.role in ['author', 'supervisor']:
                return '/worker/dashboard/'  # Change to your worker dashboard URL
            else:
                return '/posts/'  # Change to your general post URL
        return super().get_success_url()

def custom_logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out due to inactivity.")
    return redirect('post') 

@login_required
def user_profile(request):
    if user.is_authenticated:
        user= request.user
        return render(request, 'Users/profile.html', {'user': user})
    
def admin_dashbord(request):
    return render(request, 'admin_dashbord/admin.html')


@csrf_exempt
def check_email_availability(request):
    email = request.POST.get("email")
    try:
        user = CustomUser.objects.filter(email=email).exists()
        if user:
            return HttpResponse(True)
        return HttpResponse(False)
    except Exception as e:
        return HttpResponse(False)

   







# Create your views here.
