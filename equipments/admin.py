from django.contrib import admin
from .models import Equipment


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("type", "serial", "brand", "model", "purchase_date", "price")


admin.site.register(Equipment, EquipmentAdmin)
