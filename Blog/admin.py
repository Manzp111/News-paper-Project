from django.contrib import admin
from Blog.models import Post

admin.site.site_header='SOLVIT News'
admin.site.site_title='SOLVIT Administration'
admin.site.index_title='SOLVIT Administration'

    
@admin.register(Post)
class PostDisplay(admin.ModelAdmin):
    list_display=['author','title','publication_date','is_published']
    





