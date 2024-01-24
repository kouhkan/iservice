from django.contrib import admin

from herfeei.experts.models import (AvailableTimeExpert, Bookmark, Expert,
                                    ExpertSkill, Sample, Warranty)


@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ("user", "expert_code", "province", "city", "status")
    list_filter = ("province", "status")
    search_fields = ("user", "province", "city", "expert_code")
    list_editable = ("status", )
    list_per_page = 25
    autocomplete_fields = ("user", )
    raw_id_fields = ("user", )


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ("user", "expert")
    search_fields = ("user", "expert")
    list_per_page = 25


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ("expert", "category", "created_at")
    search_fields = ("expert", )
    list_per_page = 25


@admin.register(AvailableTimeExpert)
class AvailableTimeExpert(admin.ModelAdmin):
    list_display = ("expert", "start_time", "end_time", "date")
    search_fields = ("expert", )
    list_per_page = 25


@admin.register(Warranty)
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ("expert", )
    search_fields = ("expert", )
    list_per_page = 25


@admin.register(ExpertSkill)
class ExpertSkillAdmin(admin.ModelAdmin):
    list_display = ("expert", )
    search_fields = ("expert", )
    list_per_page = 25
