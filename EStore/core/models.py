from django.db import models
from prof.models import UserProfile


class Contract(models.Model):
    kind = models.CharField(max_length=255)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.kind


class Part(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    # transactions = models.ManyToManyField('Transaction')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(max_length=255)
    count = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SecondHandPart(models.Model):
    name = models.CharField(max_length=255, unique=True, primary_key=True)
    # transactions = models.ManyToManyField('Transaction')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Transaction(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, null=True, blank=True)
    total_items = models.PositiveIntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    purchase= models.ForeignKey('Purchase', on_delete=models.PROTECT, null=True, blank=True)
    discount = models.FloatField(null=True, blank=True)

    def calculate_discounted_amount(self):
        if self.discount:
            return self.total_amount - (self.total_amount * (self.discount / 100))
        return self.total_amount

    def __str__(self):
        return f"Transaction {self.id} by {self.user}"


class Purchase(models.Model):
    parts = models.ManyToManyField(Part, blank=True)
    second_hand_parts = models.ManyToManyField(SecondHandPart, blank=True)
    contracts = models.ManyToManyField(Contract, blank=True)
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"Purchase by {self.user}"