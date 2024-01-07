from django.contrib import admin

from herfeei.dashboards.models import Rule


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "enable")
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("enable", )
    list_editable = ("enable", )
