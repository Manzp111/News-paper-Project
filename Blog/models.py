from django.db import models
from django.contrib.auth.models import User
from Accounts.models import CustomUser


class Post(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    publication_date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    is_published=models.BooleanField(default=False,blank=True)

    def __str__(self):
        return f"{self.author.email}-{self.title}-{self.publication_date}-{self.is_published}"
    
    def save(self,*args,**kwargs):
        self.title=self.title.capitalize()
        # self.content=self.title.
        super().save(*args,**kwargs)
