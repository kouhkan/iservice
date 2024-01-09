from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from herfeei.services.models import City, Province, ServiceCategory


class CityTabularAdmin(admin.TabularInline):
    model = City
    extra = 3
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name",)
    list_per_page = 25
    inlines = (CityTabularAdmin,)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(TreeAdmin):
    form = movenodeform_factory(ServiceCategory)
    prepopulated_fields = {"slug": ("title",)}
