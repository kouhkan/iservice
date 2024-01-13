from django.contrib import admin

from herfeei.home.models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ("slug", "caption", "weight", "created_at")
    list_per_page = 25
    list_filter = ("status",)
    prepopulated_fields = {"slug": ("title", "caption")}

