from django.urls import path
from django.contrib.auth import views as auth_views

from Blog.views import home,post,add_new,base,edit_story,story_list,delete_story

urlpatterns = [
   path('home/',home,name='home'),
   path('',post,name='post'),
   path('add/post/',add_new,name='add_new'),
   path('base/',base,name='base'),
   path('edit/<int:post_id>/',edit_story,name='edit_story'),
   path('list/',story_list,name='story_list'),
   path('delete/<int:post_id>',delete_story,name='delete_story'),

   # path('user/',sign_up,name='user'),
   # path('user/login/', MyLoginView.as_view(), name='login'),
   # path('create/account/',create_account,name='account'),
   


]
