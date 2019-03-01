from django.contrib import admin

# Register your models here.

from .models import Article

# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title','author','created','update']

admin.site.register(Article)