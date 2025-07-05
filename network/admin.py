from django.contrib import admin
from django.utils.html import format_html
from .models import NetworkNode, Contact, Product


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'node_type', 'hierarchy_level', 'supplier_link', 'debt', 'created_at')
    list_filter = ('contact__city', 'node_type', 'contact__country')
    search_fields = ('name', 'contact__email', 'contact__country')
    actions = [clear_debt]

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html('<a href="{}">{}</a>',
                               f'/admin/network/networknode/{obj.supplier.id}/change/',
                               obj.supplier.name)
        return "-"

    supplier_link.short_description = 'Поставщик'

    def hierarchy_level(self, obj):
        return obj.hierarchy_level

    hierarchy_level.short_description = 'Уровень иерархии'
