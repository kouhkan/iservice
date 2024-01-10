from django.contrib import admin

from herfeei.notifications.models import Notification, UserNotification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "level", "created_at")
    list_filter = ("level",)
    list_per_page = 25
    prepopulated_fields = {"slug": ("title",)}


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "notification", "status", "created_at")
    search_fields = ("user", "notification")
    list_per_page = 25
