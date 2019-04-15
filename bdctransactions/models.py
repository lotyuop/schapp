from django.db import models
from accounts.models import BdcProfile
from django.contrib.auth.models import User

# Create your models here.
class BdcClient(models.Model):
    bdc_id = models.ForeignKey(BdcProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=16)
    email = models.EmailField(verbose_name='Email')
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['bdc_id', 'phone'], name='unique_client')]

    def __str__(self):
        return self.name

class Currency(models.Model):
    name=models.CharField(max_length=40, unique=True)
    currency_symbol = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name

class Banks(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class BdcTranzactions(models.Model):
    Bdc_id = models.ForeignKey(BdcProfile, on_delete=models.CASCADE)
    client = models.ForeignKey(BdcClient, on_delete=models.CASCADE)
    currency_sold = models.ForeignKey(Currency, on_delete=models.CASCADE,verbose_name="Currency Sold", related_name="trans_sold_currency")
    sold_amount = models.DecimalField(max_digits=19, decimal_places=4, verbose_name="Amount Sold")
    currency_bought = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Currency Bought", related_name="trans_bought_currency")
    bought_amount = models.DecimalField(max_digits=19, decimal_places=4, verbose_name="Amount Bought")
    client_bank = models.ForeignKey(Banks, on_delete=models.CASCADE, verbose_name="Client Bank")
    client_acct = models.IntegerField(blank=True, verbose_name="Client Account")
    trans_date = models.DateField()
    trans_added_on = models.DateTimeField(auto_now_add=True)
    trans_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(blank=True)
    Updated_by = models.CharField(max_length=5)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.client.name


class BdcTranzactions_Archive(models.Model):
    Bdc_id = models.ForeignKey(BdcProfile, on_delete=models.CASCADE)
    client = models.ForeignKey(BdcClient, on_delete=models.CASCADE)
    currency_sold = models.ForeignKey(Currency, on_delete=models.CASCADE,verbose_name="Currency Sold", related_name="archive_sold_currency")
    sold_amount = models.DecimalField(max_digits=19, decimal_places=4, verbose_name="Amount Sold")
    currency_bought = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name="Currency Bought", related_name="archive_bought_currency")
    bought_amount = models.DecimalField(max_digits=19, decimal_places=4, verbose_name="Amount Bought")
    client_bank = models.ForeignKey(Banks, on_delete=models.CASCADE, verbose_name="Client Bank")
    client_acct = models.IntegerField(blank=True, verbose_name="Client Account")
    trans_date = models.DateField()
    trans_added_on = models.DateTimeField(auto_now_add=True)
    trans_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(blank=True)
    Updated_by = models.CharField(max_length=5)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.client.name

