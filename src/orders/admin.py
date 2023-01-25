from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at', 'closed_at')
    list_filter = ('status', 'customer', 'created_at')
