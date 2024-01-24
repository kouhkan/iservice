from django.contrib import admin

from herfeei.dashboards.models import Contact, Faq, FaqCategory, Rule


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "status")
    prepopulated_fields = {"slug": ("title", )}
    list_filter = ("status", )
    list_editable = ("status", )


@admin.register(Faq)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "category", "created_at", "status")
    list_filter = ("status", )
    list_per_page = 25
    prepopulated_fields = {"slug": ("title", )}


@admin.register(FaqCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "status")
    list_filter = ("status", )
    list_per_page = 25
    prepopulated_fields = {"slug": ("title", )}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "created_at")
    search_fields = ("title", "content")
    list_per_page = 25
    prepopulated_fields = {"slug": ("title", )}
