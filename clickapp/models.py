from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class TariffCalc(models.Model):
    """
    Define Tariff Calculator object for model form
    """

    WAREHOUSE_LIST = [("de", "DE"), ("ch", "CH")]

    CUSTOMER_LIST = [("de", "DE"), ("ch", "CH"), ("fr", "FR"), ("us", "US")]

    TAX_RATE_DICT = {0.19: "19%", 0.077: "7.7%", 0: "Steuerfrei"}

    warehouse = models.CharField(max_length=2, choices=WAREHOUSE_LIST)
    customer = models.CharField(max_length=2, choices=CUSTOMER_LIST)
    net = models.DecimalField(
        max_digits=9, decimal_places=2, validators=[MinValueValidator(1)]
    )
    tax_rate = models.DecimalField(max_digits=4, decimal_places=3, blank=True)
    gross = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    classification = models.CharField(max_length=2, blank=True)
