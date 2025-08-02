from django.db import models
from django.contrib.auth.models import AbstractUser


user_roles = (
    ('admin', 'Admin'),
    ('supervisor', 'Supervisor'),
    ('author', 'Author'),
    ('subscriber', 'Subscriber'),
)
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=user_roles, default='subscriber')
   



    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['role']
        verbose_name = 'Custom User'
        verbose_name_plural = 'Users'
# class SuperVisor(CustomUser):
#     user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name_plural = "Supervisors"


# class Author(CustomUser):
#     user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user

  







        

# Create your models here.
