from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from herfeei.notifications.models import (BaseNotification,
                                          NotificationCategory,
                                          NotificationOption, UserNotification)


@admin.register(NotificationCategory)
class NotificationCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(NotificationCategory)
    list_display = ("title", "slug", "created_at")
    search_fields = ("title", )
    prepopulated_fields = {"slug": ("title", )}
    list_per_page = 25


@admin.register(BaseNotification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "level", "created_at")
    list_filter = ("level", )
    list_per_page = 25
    prepopulated_fields = {"slug": ("title", )}


@admin.register(NotificationOption)
class NotificationOptionTabularAdmin(admin.ModelAdmin):
    list_display = ("item", "value")
    list_per_page = 25


@admin.register(UserNotification)
class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "notification", "status", "created_at")
    search_fields = ("user", "notification")
    list_per_page = 25
