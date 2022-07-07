from django.contrib import admin

from vendorapp.models import SettingsBanner, SettingsServices, SettingsSocialLinks, Vendor, Vendor_Packaging, Vendor_ShippingMethod

# Register your models here.
admin.site.register(Vendor)
admin.site.register(SettingsBanner)
admin.site.register(SettingsServices)
admin.site.register(SettingsSocialLinks)
admin.site.register(Vendor_Packaging)
admin.site.register(Vendor_ShippingMethod)