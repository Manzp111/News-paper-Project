from django.db import models
import os
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify

from Accounts.models import CustomUser
from datetime import datetime

def get_upload_path(instance, filename):
    category = instance.category or "general"
    # Optional: make filename unique using timestamp
    filename_base, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{filename_base}_{timestamp}{ext}"
    return f'post_images/{category}/{new_filename}'

class Post(models.Model):
    CATEGORY_CHOICES = [
        
        ('sports', 'Sports'),
        ('entertainment', 'Entertainment'),
        ('politics', 'Politics'),
        ('technology', 'Technology'),
        ('health', 'Health'),
        ('business', 'Business'),
        ('general', 'General'),
    ]
    
    title=models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    Content_image=models.ImageField(upload_to='content_image/',null=True,blank=True)
    content=RichTextUploadingField()
    publication_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_published=models.BooleanField(default=False,blank=True)
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')

    def __str__(self):
        return f"{self.author.email}-{self.title}-{self.publication_date}-{self.is_published}"
    


    
    def save(self,*args,**kwargs):
        self.title=self.title.capitalize()
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    






class Contact(models.Model):
   
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    comment=models.TimeField(max_length=255)
    date=models.DateTimeField(auto_now=True)
    read=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.date}"
class VisitorPost(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    publication_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='visitor_posts')
    is_published=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f"{self.author.email}-{self.title}-{self.publication_date}-{self.is_published}"
    
    def save(self,*args,**kwargs):
        self.title=self.title.capitalize()
        super().save(*args,**kwargs)

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')  # 👈 Add this
    created_at = models.DateTimeField(auto_now_add=True)
    time=models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('post', 'user')  

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField(blank=True,null=True)
    comment=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    is_publish=models.BooleanField(default=False)
    read=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sender_name} - {self.comment} - {self.created_at}"