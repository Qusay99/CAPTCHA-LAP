from django.contrib import admin
from django.utils.translation import activate
from .models import Content, Comment, Document

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("header", "body", "content", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("header", "body")
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("header", "slug", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("header", "description")
    actions = ['approve_contents']
    prepopulated_fields = {"slug": ("header",)}
    
    def approve_contents(self, request, queryset):
        queryset.update(active=True)

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "uploaded_on", "description" ,"docfile")
    actions = ["approve_documents"]

    def approve_documents(self, request, queryset):
        queryset.update(active=True)
    

