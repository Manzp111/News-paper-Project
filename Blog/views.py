from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import datetime
from django.contrib.auth.decorators import login_required

#third_parties

from Blog.models import Post
from Blog.forms import PostForm
from Blog.decorators import SupervisorRequired, AuthorRequired


#from Accounts.models import CustomUser
from Accounts.models import CustomUser


# class MyLoginView(LoginView):
#     template_name = 'login.html'  # Your login template
#     redirect_authenticated_user = True
#     next_page = reverse_lazy('home')



def base(request):
    return render(request,'base.html')

@login_required
def home(request):
    # author=Author.objects.all()
    return  render(request,'home/index.html')
    # return render(request,'home/index.html',{'authors':author})

def post(request):
    post=Post.objects.all()
    return render(request,'home/post.html',{'posts':post})

@login_required
@AuthorRequired()
def add_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        form.request = request
        if form.is_valid():

            form.save()
            return redirect('post')
        
    else:
        form=PostForm()
 
    return render(request,'home/post_new.html',{'form':form})

            
 
@login_required
@AuthorRequired()

def edit_story(request,post_id):
    post=get_object_or_404(Post,id=post_id)
    if request.method == "POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post')
    else:
        form=PostForm(instance=post)
    return render(request,'home/edit_post.html',{'form':form})


@SupervisorRequired()
def delete_story(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post')
    return render(request, 'home/delete_post.html', {'post': post})


@login_required()
@SupervisorRequired()
def story_list(request):
    posts = Post.objects.all()
    return render(request, 'home/listPost.html', {'posts': posts})


# def index(request):
#     request.session.set_test_cookie()

#     num_visits = request.session.get('num_visits', 0)
#     request.session['num_visits'] = num_visits + 1

#     return HttpResponse(f"Visit count: {request.session['num_visits']}")

# def about(request):
#     if request.session.test_cookie_worked():
#         print("Cookie Tested!")
#         request.session.delete_test_cookie()
#     return HttpResponse("About page")

    


# def sign_up(request):
#     form = UserForm()
#     if request.method == 'POST':
    
#         form = UserForm(request.POST)
#         if form.is_valid():
#             User.objects.create(
#                 username=form.cleaned_data['username'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password'])
#             return redirect('post')
#     return render(request, 'home/signUp.html', {'form': form})

# def login(request):
#     form=LoginForm()

#     return  render(request,'login.html',{'form':form})

# def create_account(request):
#     form = SignUpForm()
#     if request.method=='POST':
#         form=SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("account created!")
#     return render(request,'home/createAccount.html',{'forms':form})






    

        
        


        




#  if form.is_valid():
#             User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password']  # hashed automatically
#             )





#from django.shortcuts import render
#from djjango.http import HttpResponse

def home(request):
    return HttpResponse()