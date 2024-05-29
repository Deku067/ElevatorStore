from django.contrib import admin
from .models import Contract, Part, SecondHandPart, Transaction, Purchase


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('kind', 'count')


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'kind', 'count', 'manufacturer')
    search_fields = ('name', 'kind', 'manufacturer')
    list_filter = ('kind', 'manufacturer')


@admin.register(SecondHandPart)
class SecondHandPartAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'kind', 'manufacturer', 'count')
    search_fields = ('name', 'kind', 'manufacturer')
    list_filter = ('kind', 'manufacturer')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_items', 'total_amount', 'discount', 'calculate_discounted_amount')
    readonly_fields = ('calculate_discounted_amount',)

    def calculate_discounted_amount(self, obj):
        return obj.calculate_discounted_amount()
    calculate_discounted_amount.short_description = 'Discounted Amount'


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('parts', 'second_hand_parts', 'contracts')
    search_fields = ('user__username',)  # Allows searching purchases by user's username
    list_filter = ('parts', 'second_hand_parts', 'contracts')

# Removing the redundant admin.site.register calls

# admin.site.register(Part)
# admin.site.register(SecondHandPart)
# admin.site.register(Contract)
