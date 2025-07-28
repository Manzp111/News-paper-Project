from django import forms
from Blog.models import Post
from django.contrib.auth.models import User
import datetime


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content']

    def clean(self):
        super().clean()
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if not title or not content:
            raise forms.ValidationError("Title and content cannot be empty.")
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        if len(content) < 20:
            raise forms.ValidationError("Content must be at least 20 characters long.")
    def __init__(self,*args,**kwargs):
        self.request=kwargs.pop('request', None)
        super().__init__(*args,**kwargs)

    
    def save(self, commit=True):
        post = super().save(commit=False)
        if self.request and self.request.user.is_authenticated:
            post.author = self.request.user
            if commit:
                post.save()
            return post
        return None
    
    

    
    




        
# def add_product(request):
#     property=property.pbjects.all()
#     if request.method=='POST':
#         property=PostForm(request.POST)   {% csrf_token %}
#         if property.is_valid():
#             property.save()




    
