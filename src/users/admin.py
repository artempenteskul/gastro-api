from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'date_joined', 'last_login')
    list_display_links = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')
    empty_value_display = '-'
    list_per_page = 50
