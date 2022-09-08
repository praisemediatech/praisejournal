from django.contrib import admin

from .models import Post, Tag, Comment, Reply, Categories

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created', 'verified']

class ReplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'reply', 'created', 'verified']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date']
    prepopulated_fields = {'slug':('title',)}

    fieldsets = [
        ('Post Information',    {'fields': ['title', 'category', 'tag', 'author']}),
        ('Content',             {'fields': ['post_image', 'section_one', 'quote', 'quote_author','quote_image','section_two']}),
        ('Other Information',   {'fields': ['slug']}),
    ]

    

class categoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'created']

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag', 'created']



admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Categories, categoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Reply, ReplyAdmin)