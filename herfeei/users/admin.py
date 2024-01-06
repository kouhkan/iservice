from django.contrib import admin

from herfeei.users.models import BaseUser, Profile


@admin.register(BaseUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "is_superuser")
    filter = ("role",)
    search_fields = ("username", "email")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name")
    search_fields = ("user",)
