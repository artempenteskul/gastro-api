from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')
    list_display_links = ('username', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'username', 'email', 'phone')
    empty_value_display = '-'
    list_per_page = 50
