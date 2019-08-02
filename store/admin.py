from django.contrib import admin

from store.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'status')
    list_display_links = ('name', 'user', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
