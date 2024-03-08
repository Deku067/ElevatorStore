from django.db import models
from purchase.models import Basket_buy
from User.models import Manager

# Create your models here.
class parts(models.Model):
    part_name = models.CharField(max_length=255,unique = True, primary_key=True)
    basket_id = models.ForeignKey(Basket_buy, on_delete=models.CASCADE, null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    kind = models.CharField(max_length=255)
    count_p = models.PositiveIntegerField()
    manufacturer = models.CharField(max_length=255)

    #add_part()
    #delete_part()
    #update_part()
    #Search_part()
    #Show_part
    # compare_parts()
    # part_change()

class second_hand_parts(models.Model):
    part_name_s = models.CharField(max_length=255,unique = True, primary_key=True)
    basket_id = models.ForeignKey(Basket_buy, on_delete=models.CASCADE, null=True,blank=True)
    price_s = models.DecimalField(max_digits=10, decimal_places=2)
    kind_s = models.CharField(max_length=255)
    manufacturer_s = models.CharField(max_length=255)
    count_s = models.PositiveIntegerField()
    #add_s_part()
    #delete_s_part()
    #update_s_part()
    #Search_s_part()
    #Show_s_part
    # compare_s_parts()
    # part_s_change()

class Contract(models.Model):
    basket_id = models.ForeignKey(Basket_buy, on_delete=models.CASCADE, null=True,blank=True)
    contractKind = models.CharField(max_length=255)
    count_c = models.PositiveIntegerField()
    # add_count()
    # delete_count()
    # update_count()
    # Search_count()
    # Show_count()

class Change(models.Model):
    
    Username_id = models.ForeignKey(Manager, on_delete=models.CASCADE, null=True,blank=True)
    Contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True,blank=True)
    basket_id = models.ForeignKey(Basket_buy, on_delete=models.CASCADE, null=True,blank=True)
    parts_name = models.ForeignKey(parts, on_delete=models.CASCADE, null=True,blank=True)
    parts_s_name = models.ForeignKey(second_hand_parts, on_delete=models.CASCADE, null=True,blank=True)
    
