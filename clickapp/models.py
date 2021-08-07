from django.db import models

# Create your models here.
class TariffCalc(models.Model):
    WAREHOUSE_LIST = [
        ('de', 'DE'),
        ('ch', 'CH')
    ]

    CUSTOMER_LIST = [
        ('de', 'DE'),
        ('ch', 'CH'),
        ('fr', 'FR'),
        ('us', 'US')
    ]

    CLASSIFICATION_DICT = {
        'ch': 'EU',
        'de': 'EU',
        'fr': 'EU',
        'us': 'US'
    }

    INTERNAL_TAX_DICT = {
        'de': 0.19,
        'ch': 0.077,
        'us': 0,
    }

    TAX_RATE_DICT = {
        0.19: '19%',
        0.077: '7.7%',
        0: 'Steuerfrei'
    }

    warehouse = models.CharField(max_length=2, choices=WAREHOUSE_LIST)
    customer = models.CharField(max_length=2, choices=CUSTOMER_LIST)
    net = models.DecimalField(max_digits=9, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=3)
    gross = models.DecimalField(max_digits=10, decimal_places=2)
    classification = models.CharField(max_length=2)

    def __str__(self):
        pass
