from django import forms
from Blog.models import Post,Contact,VisitorPost,VisitorPost
from django.contrib.auth.models import User
import datetime


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','content','category']
        
    def __init__(self,*args,**kwargs):
        self.request=kwargs.pop('request', None)
        super().__init__(*args,**kwargs)
        # Add custom styling to the category field
        self.fields['category'].widget.attrs.update({
            'class': 'shadow-xs bg-gray-50 border border-gray-300 text-black-500 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5'
        })

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

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields=['first_name','last_name','email','comment']

    def clean(self):
        super().clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        comment = self.cleaned_data.get('comment')
        if not first_name or not last_name or not email or not comment:
            raise forms.ValidationError("All fields are required.")
        if len(comment) < 10:
            raise forms.ValidationError("Comment must be at least 10 characters long.")   

class VisitorPostForm(forms.ModelForm):
    class Meta:
        model=VisitorPost
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
    
class VisitorPostForm(forms.ModelForm):
    class Meta:
        model = VisitorPost
        fields = ['title', 'content']

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

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

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




    
