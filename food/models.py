from django.db import models

# Create your models here.
class Popular(models.Model):
    id = models.BigAutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_pic = models.ImageField()
    item_price = models.IntegerField()

    def __str__(self):
        return self.item_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=2000)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return self.username