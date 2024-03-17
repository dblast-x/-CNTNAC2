from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, through="OrderItem")
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
