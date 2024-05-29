from django.contrib import admin
from .models import UserProfile, Comment

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'phone', 'email_address')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'content')
