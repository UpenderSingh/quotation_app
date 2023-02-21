from django.db import models
from customerapp.models import CommonInfo, CustomerProfile


class Item(CommonInfo):
    name = models.CharField(max_length=200, blank=False)
    price = models.FloatField(blank=False,)
    description = models.TextField(blank=True)
    quantity = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Quotation(CommonInfo):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE,)
    quote_expiry_date = models.DateTimeField()
    total = models.CharField(max_length=50)
    sub_total = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return str(self.item)