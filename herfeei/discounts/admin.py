from django.contrib import admin

from herfeei.discounts.models import Discount


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ("title", "token", "start_date", "end_date", "created_at",
                    "expired")
    search_fields = ("title", "token", "description")
    raw_id_fields = ("user", "service_category")
    prepopulated_fields = {"slug": ("title", )}
    list_per_page = 25
