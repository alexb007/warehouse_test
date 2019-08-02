from django.contrib import admin

from store.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_display_links = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
