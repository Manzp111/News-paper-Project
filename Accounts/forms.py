from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class SignUpForm(forms.Form):
    first_name=forms.CharField(max_length=255,label="First Name")
    last_name=forms.CharField(max_length=255,label="last name")
    email=forms.EmailField(label="E-mail",required=True,widget=forms.EmailInput(attrs={'placeholder':'enter your email here'}))
    password=forms.CharField(widget=forms.PasswordInput(),label="Password")
    password2=forms.CharField(widget=forms.PasswordInput(),label="Confirm password")
    # sign_up_date=forms.DateTimeField(label="Sign Up Date",required=False)

 
    
    def clean(self):
        super().clean()
        password=self.cleaned_data.get('password')
        password2=self.cleaned_data.get('password2')
        if password and password2 and  password != password2:
            raise forms.ValidationError("Passwords do not match")
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        
    
    
        
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        else:
            return email
        
    def save(self):
        return User.objects.create_user(
            username=self.cleaned_data.get('email'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            password=self.cleaned_data.get('password'),
            # sign_up_date=datetime.datetime.now() 
        )
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

     
        