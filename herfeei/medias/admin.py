from django.contrib import admin

from herfeei.medias.models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ("file", "_file", "user", "type", "usage")
    list_filter = ("type", "usage")
    search_fields = ("file", "user")
    raw_id_fields = ("user",)
