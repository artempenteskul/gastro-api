from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    fields = ('id', 'customer', 'status', ('created_at', 'closed_at'))
    list_display = ('id', 'customer', 'status', 'created_at', 'closed_at')
    list_filter = ('status', 'customer', 'created_at')
    readonly_fields = ('id', 'customer', 'status', 'created_at', 'closed_at')
    list_select_related = ('customer',)
    search_fields = ('id', 'customer')
    empty_value_display = '-'
    list_per_page = 50
