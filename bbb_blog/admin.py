from django.contrib import admin
from bbb_blog.models import Category, Post
# Register your models here.

admin.site.register(Category)
admin.site.register(Post)