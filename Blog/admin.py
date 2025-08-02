from django.contrib import admin
from Blog.models import Post,Contact,VisitorPost,Like,Comment
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import messages

# admin.site.site_header='Kigali Trends'
# admin.site.site_title='Kigali Trends Admin'
# admin.site.index_title='Kigali Trends'

@admin.action(description="mark as publish")
def publish(modeladmin,request,queryset):
    updated=queryset.update(is_published=True)
    messages.success(request,f'Published')

@admin.action(description="unpublish") 
def UnPublish(modeladmin, request, queryset):
    updated=queryset.update(is_published=False)
    messages.info(request,f'uPost is unpublished ')
@admin.register(Post)
class PostDisplay(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display=['title','publication_date','is_published','author','preview_link']
    list_filter = ('is_published', 'author', 'publication_date')
    search_fields = ('title', 'content')
    list_per_page = 10
    actions=[publish,UnPublish]

    def preview_link(self, obj):
        if obj.pk and obj.slug:
            url = reverse('story_detail', kwargs={'slug': obj.slug})
            return format_html(
                '<a class="button" href="{}" target="_blank">Preview</a>',
                url
            )
        return "-"
    preview_link.short_description = "Preview"

@admin.action(description="mark as publish")
def read(modeladmin,request,queryset):
    updated=queryset.update(read=True)
    messages.success(request,f'marked as visited')
class ContactDisplay(admin.ModelAdmin):
    list_display=['first_name','last_name','email','comment','date']
    search_fields=['first_name','last_name','email']
    list_filter=['date','read']
    actions=[read]


@admin.register(VisitorPost)
class VisitorPostDisplay(admin.ModelAdmin):
    list_display=['author','title','publication_date','is_published']
    search_fields=['title','author__email']
    list_filter=['publication_date','is_published']
    actions=[publish,UnPublish]


@admin.register(Like)
class LikeDisplay(admin.ModelAdmin):
    list_display=['post','created_at']
    search_fields=['post__title']
    list_filter=['created_at']
 

@admin.register(Comment)
class CommentDisplay(admin.ModelAdmin):
    list_display=['post','sender_email','comment']
    search_fields=['post','comment']
    list_filter=['is_publish','read']
    actions=[publish,UnPublish,read]





