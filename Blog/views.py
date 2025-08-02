from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#third_parties

from Blog.models import Post,Comment,Contact,VisitorPost,Like
from Blog.forms import PostForm,CommentForm,ContactForm, VisitorPostForm
from Blog.decorators import SupervisorRequired, AuthorRequired
from Accounts.models import CustomUser



def base(request):
    return render(request,'base.html')

@login_required
def supervisor_dashboard(request):
    # Get counts of each model
    post_count = Post.objects.count()
    contact_count = Contact.objects.count()
    visitor_post_count = VisitorPost.objects.count()
    like_count = Like.objects.count()
    comment_count = Comment.objects.count()

    context = {
        'post_count': post_count,
        'contact_count': contact_count,
        'visitor_post_count': visitor_post_count,
        'like_count': like_count,
        'comment_count': comment_count,
    }

    return render(request, 'supervisor/index.html', context)

def author(request):
    return render(request,'Athor/index.html')

@login_required
def home(request):
    # author=Author.objects.all()
    return  render(request,'home/index.html')
    # return render(request,'home/index.html',{'authors':author})

def post(request):
    # imge=
    posts = Post.objects.filter(is_published=True).order_by('-publication_date')
    return render(request,'home/post.html',{'posts':posts})

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
 
    return render(request,'supervisor/post_new.html',{'form':form})
        
 
 
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
    return render(request,'supervisor/edit_post.html',{'form':form})


@SupervisorRequired()
def delete_story(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('post')
    return render(request, 'supervisor/delete_post.html', {'post': post})


@login_required()
@SupervisorRequired()
def story_list(request):
    posts = Post.objects.all()
    return render(request, 'supervisor/listPost.html', {'posts': posts})


def story_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        content = request.POST.get("content")
        if content and request.user.is_authenticated:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )
            return redirect('story_detail', slug=slug)

    comments = post.comments.order_by("-created_at") 


    
    return render(request, 'home/story_detail.html', {'post': post,'comments': comments })

def sports_news(request):
    posts = Post.objects.filter(category='sports', is_published=True).order_by('-publication_date')
    return render(request, 'home/category_posts.html', {'posts': posts, 'category': 'Sports'})

def entertainment_news(request):
    posts = Post.objects.filter(category='entertainment', is_published=True).order_by('-publication_date')
    return render(request, 'home/category_posts.html', {'posts': posts, 'category': 'Entertainment'})

def politics_news(request):
    posts = Post.objects.filter(category='politics', is_published=True).order_by('-publication_date')
    return render(request, 'home/category_posts.html', {'posts': posts, 'category': 'Politics'})

def technology_news(request):
    posts = Post.objects.filter(category='technology', is_published=True).order_by('-publication_date')
    return render(request, 'home/category_posts.html', {'posts': posts, 'category': 'Technology'})

def health_news(request):
    posts = Post.objects.filter(category='health', is_published=True).order_by('-publication_date')
    return render(request, 'home/category_posts.html', {'posts': posts, 'category': 'Health'})

def business_news(request):
    posts = Post.objects.filter(category='business', is_published=True).order_by('-publication_date')
    return render(request, 'home/category_posts.html', {'posts': posts, 'category': 'Business'})

@csrf_exempt
def like_post(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        Like.objects.create(post=post)
        return JsonResponse({"likes_count": post.likes.count()})
    return JsonResponse({"error": "Invalid request"}, status=400)