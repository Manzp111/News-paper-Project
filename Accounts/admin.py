from django.contrib import admin
from django.contrib import messages
from .models import CustomUser



@admin.action(description="mark as inactive")
def deactivate(modeladmin,request,queryset):
    updated=queryset.update(is_active=False)
    messages.success(request,f'status of {updated} is inactive')

@admin.action(description="mark as active") 
def activate(modeladmin, request, queryset):
    updated=queryset.update(is_active=True)
    messages.info(request,f'status of {updated} is active')

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email','role')
    search_fields = ('role','email')
    list_filter = ('role',)
    ordering = ('role',)
    actions=[activate,deactivate]








