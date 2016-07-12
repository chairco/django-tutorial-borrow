# faships/admin.py
from django.contrib import admin

from .models import Faship, Device, Station

from import_export.admin import ImportExportMixin, ExportActionModelAdmin
from import_export import resources, widgets, fields
from import_export.widgets import ForeignKeyWidget


class StationResource(resources.ModelResource):

    class Meta:
        model = Station
        fields = ('id','name')


class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1


@admin.register(Faship)
class FashipAdmin(admin.ModelAdmin):
    list_display = ['owner', 'purpose', 'created_at']
    inlines = [DeviceInline]


@admin.register(Device)
class FashipAdmin(admin.ModelAdmin):
    list_display = ['isn', 'unit_no', 'config']


@admin.register(Station)
class StationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name')
    resource_class = StationResource 
