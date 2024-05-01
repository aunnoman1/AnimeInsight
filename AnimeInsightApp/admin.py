from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,AnimeMetadata,Profile

# Register your models here.

class ProfileInline(admin.StackedInline):
    model=Profile
    can_delete=False

class CustomUserAdmin(UserAdmin):
    inlines=(ProfileInline,)
admin.site.register(User, CustomUserAdmin)

admin.site.register(AnimeMetadata)