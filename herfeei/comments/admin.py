from django.contrib import admin

from herfeei.comments.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "expert", "description", "rate", "created_at", "status")
    list_filter = ("status",)
    search_fields = ("user", "expert", "description")
    list_per_page = 50
    raw_id_fields = ("user", "expert")
    list_editable = ("status",)
