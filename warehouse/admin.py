from django.contrib import admin

from warehouse.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    list_display_links = ('name', 'status')
    list_filter = ('status',)
    search_fields = ('name',)
    ordering = ('-created_at', 'name', 'status')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['id', 'name', ]
        return []
