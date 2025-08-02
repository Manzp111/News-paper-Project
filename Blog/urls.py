from django.urls import path,include
from django.contrib.auth import views as auth_views

from Blog.views import (
    home, post, add_new, base, edit_story, story_list, delete_story, story_detail,
    sports_news, entertainment_news, politics_news, technology_news, health_news, business_news,
    supervisor_dashboard,like_post
   
)

urlpatterns = [
   path('home/',home,name='home'),
   path('',post,name='post'),

   path('add/post/',add_new,name='add_new'),
   path('ckeditor/', include('ckeditor_uploader.urls')),
   path('base/',base,name='base'),
   path('edit/<int:post_id>/',edit_story,name='edit_story'),
   path('list/',story_list,name='story_list'),
   path('delete/<int:post_id>',delete_story,name='delete_story'),
   path('story/<slug:slug>/',story_detail, name="story_detail"),
   
   # Category-specific URLs
   path('sports/', sports_news, name='sports'),
   path('entertainment/', entertainment_news, name='entertainment'),
   path('politics/', politics_news, name='politics'),
   path('technology/', technology_news, name='technology'),
   path('health/', health_news, name='health'),
   path('business/', business_news, name='business'),
   path('like-post/<int:post_id>/', like_post, name='like_post'),


   # Role-specific dashboard URLs
   path('supervisor/dashboard/', supervisor_dashboard, name='worker_dashboard'),
#    path('dashboard/', dashboard, name='dashboard'),
#    path('admin/dashboard/', admin_dashboard, name='admin_dashboard'),
#    path('author/dashboard/', author_dashboard, name='author_dashboard'),
#    path('subscriber/dashboard/', subscriber_dashboard, name='subscriber_dashboard'),
   
#    # Admin management URLs
#    path('admin/users/', admin_manage_users, name='admin_manage_users'),
#    path('admin/posts/', admin_manage_posts, name='admin_manage_posts'),
   
#    # Supervisor management URLs
#    path('supervisor/approve/', supervisor_approve_posts, name='supervisor_approve_posts'),
#    path('supervisor/approve/<int:post_id>/', supervisor_approve_post, name='supervisor_approve_post'),

#    # path('user/',sign_up,name='user'),
#    # path('user/login/', MyLoginView.as_view(), name='login'),
#    # path('create/account/',create_account,name='account'),
]
