from django.db import models
from decimal import Decimal
from prof.models import UserProfile

class Product(models.Model):
    PARTS = 'PART'
    SECOND_HAND_PARTS = 'SHP'
    CONTRACT = 'CON'

    CATEGORY_CHOICES = [
        (PARTS, 'Parts'),
        (SECOND_HAND_PARTS, 'Second Hand Parts'),
        (CONTRACT, 'Contract'),
    ]

    COUNTRY_CHOICES = [
        ('USA', 'United States'),
        ('UK', 'United Kingdom'),
        ('CN', 'China'),
        ('JP', 'Japan'),
        ('IR', 'Iran'),
        ('DE', 'Germany'),
        ('SE', 'Sweden'),
        ('IT', 'Italy'),
        ('CH', 'Switzerland'),
        ('NO', 'Norway'),
        ('CA', 'Canada'),
        ('FI', 'Finland'),
        ('RU', 'Russia'),
    ]

    DEFAULT_COUNTRY = 'IR'
    DEFAULT_CATEGORY = PARTS

    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=3, choices=COUNTRY_CHOICES, default=DEFAULT_COUNTRY)
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, default=DEFAULT_CATEGORY)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='products/' ,null=True, blank=True)


    def __str__(self):
        return self.name

class Purchase(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    user = models.OneToOneField(UserProfile, on_delete=models.PROTECT, null=True, blank=True)

    def calculate_total_price(self):
        total_price = sum(product.price for product in self.products.all())
        return total_price

    def __str__(self):
        return f"Purchase by {self.user}"


class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.0'))
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, null=True, blank=True)
    discount = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.purchase:
            self.total_amount = self.purchase.calculate_total_price()
        super().save(*args, **kwargs)

    def calculate_discounted_amount(self):
        if self.discount:
            discount_amount = self.total_amount * (Decimal(self.discount) / Decimal('100'))
            return self.total_amount - discount_amount
        return self.total_amount
    
    def get_products(self):
        if self.purchase:
            return ", ".join([product.name for product in self.purchase.products.all()])
        return "No products"

    def __str__(self):
        return f"Transaction {self.id} by {self.user}"
