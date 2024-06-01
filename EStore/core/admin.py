from django.contrib import admin
from .models import Product, Purchase, Transaction
from prof.models import UserProfile


class ProductInline(admin.TabularInline):
    model = Purchase.products.through
    extra = 0
    verbose_name = "Product"
    verbose_name_plural = "Products"

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'price', 'kind', 'count', 'manufacturer')
    search_fields = ('name', 'kind', 'manufacturer')
    list_filter = ('kind', 'manufacturer')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_amount', 'get_discounted_amount', 'purchase')
    list_filter = ('user',)
    search_fields = ('user__username',)

    def get_discounted_amount(self, obj):
        return obj.calculate_discounted_amount()
    get_discounted_amount.short_description = 'Discounted Amount'



@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    inlines = [ProductInline]
    list_display = ('user', 'get_products')
    list_filter = ('user',)
    search_fields = ('user__username',)
    exclude = ('products',)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('products')

    def get_products(self, obj):
        return ", ".join([product.name for product in obj.products.all()])
    get_products.short_description = 'Products'
