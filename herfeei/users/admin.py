from django.contrib import admin

from herfeei.users.models import BaseUser, Profile, UserAvatar


@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "is_superuser")
    filter = ("role",)
    search_fields = ("username", "email")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name")
    search_fields = ("user",)


@admin.register(UserAvatar)
class UserAvatarAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "avatar", "created_at")
    list_per_page = 25
    prepopulated_fields = {"slug": ("title",)}
