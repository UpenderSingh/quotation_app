from django.db import models
from user_account.models import User


class CommonInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class CustomerProfile(models.Model):
    TYPE_CHOICES = (
        ("BILLING", "BL"),
        ("SHIPPING", "SHIPP")
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, help_text="State Abbreviation (ex: OH)")
    zipcode = models.CharField(max_length=5)
    type = models.CharField(max_length=12, choices=TYPE_CHOICES)

    def __str__(self):
        return str(self.user)
