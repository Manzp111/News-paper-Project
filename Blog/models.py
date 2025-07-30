from django.db import models
from django.contrib.auth.models import User
from Accounts.models import CustomUser


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
    content=models.TextField()
    publication_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_published=models.BooleanField(default=False,blank=True)
    category=models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')

    def __str__(self):
        return f"{self.author.email}-{self.title}-{self.publication_date}-{self.is_published}"
    
    def save(self,*args,**kwargs):
        self.title=self.title.capitalize()
        # self.content=self.title.
        super().save(*args,**kwargs)

class Contact(models.Model):
    # post
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    comment=models.TimeField(max_length=255)
    date=models.DateTimeField(auto_now=True)

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
