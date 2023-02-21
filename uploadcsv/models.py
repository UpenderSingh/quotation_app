from django.db import models
from django.conf import settings


# Create your models here.

ELECTRONICS = "ELECTRONICS"
BOOKS = "BOOKS"
COMPUTERS = "COMPUTERS"

CATEGORY_CHOICES = (
    (ELECTRONICS, ELECTRONICS),
    (BOOKS, BOOKS),
    (COMPUTERS, COMPUTERS),
)

class Product(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="product",
        null=True,
    )
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES,
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, blank=False, default=0.0
    )
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)


STATE_CHOICE = ((
 ('Bihar','Bihar'),
 ('Jharkhand','Jharkhand'),
 ('West Bengal','West Bengal'),
))

class Profile(models.Model):
  name= models.CharField(max_length=100)
  state = models.CharField(choices=STATE_CHOICE, max_length=50)
  gender= models.CharField(max_length=100)
  location= models.CharField(max_length=100)
  csf_file = models.FileField(upload_to='csvdata', blank=True)