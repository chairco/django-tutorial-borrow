# loans/admin.py
from django.contrib import admin

from .models import Loan, Device

#admin.site.register(Loan)
#admin.site.register(Device)

class DeviceInline(admin.TabularInline):
    model = Device
    extra = 1


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['owner', 'purpose', 'created_at']
    inlines = [DeviceInline]


@admin.register(Device)
class LoanAdmin(admin.ModelAdmin):
    list_display = ['isn', 'unit_no', 'config']