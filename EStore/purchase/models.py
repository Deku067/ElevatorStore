from django.db import models
from purchase.models import Basket_buy
from Services.models import parts
from Services.models import Contract
from User.models import User


# Create your models here.
class discount(models.Model):
    offer_id = models.CharField(max_length=100,unique = True)
    basket_id = models.ForeignKey(Basket_buy, on_delete=models.CASCADE, null=True,blank=True)

    # add_off()
    # delete_off()
    # update_off()
    # show_off()


class buy(models.Model):
    parts_name = models.ForeignKey(parts, on_delete=models.CASCADE, null=True,blank=True)
    basket_id = models.ForeignKey(Basket_buy, on_delete=models.CASCADE, null=True,blank=True)
    Contract_id = models.ForeignKey(Contract, on_delete=models.CASCADE, null=True,blank=True)
    Username_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)

    # show_chart()

class bill(models.Model):
    basket_id = models.ForeignKey(Basket_buy, on_delete=models.CASCADE, null=True,blank=True)
    
    # show_chart()



    

class Basket_buy(models.Model):
    count = models.PositiveIntegerField()

    # deleteOrder()
    # Processing_and_payments()
    # Show_bb()
    # addOrder()






