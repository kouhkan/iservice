from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from herfeei.services.models import City, Province, ServiceCategory, ServiceItem, Service


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


# class ServiceItemTabularAdmin(admin.TabularInline):
#     model = Service.items.through
#     extra = 3


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    list_display = ("title", "start_range", "end_range", "created_at")
    prepopulated_fields = {"slug": ("title",)}
    list_per_page = 25


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("category", "created_at")
    list_per_page = 25
    # inlines = (ServiceItemTabularAdmin,)
