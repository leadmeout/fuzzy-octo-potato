from django.db import models
from django.core.validators import MinValueValidator


class TariffCalc(models.Model):
    """A class used to represent the Tariff Calculator.

    Attributes:
        WAREHOUSE_LIST: list
            contains a list of tuples containing available warehouses

        CUSTOMER_LIST: list
            contains a list of tuples with available customers to ship to

        TAX_RATE_DICT: dict
            contains key:value pairs to display the tax rate to the user

        warehouse: str
            a dropdown field which lists elements of WAREHOUSE_LIST as choices

        customer: str
            a dropdown field which lists elements of CUSTOMER_LIST as choices

        net: Decimal
            a fixed-precision decimal number with a max_digit value of 11. This
            attribute will be validated against the MinValueValidator which
            ensures the given value is higher than 1.

            The number will always include two decimals places in POST.

        tax_rate: Decimal
            a fixed-precision decimal number with a max_digit value of 4. It
            shows 3 decimal places and is initially blank. This attribute will
            display the tax rate. Initially blank and displayed in POST.

        gross: Decimal
            a fixed-precision decimal number with a max_digit value of 12. It
            shows 3 decimal places and is initially blank. This attribute will
            display the gross total. Initially blank and displayed in POST.

        classficiation: str
            a field to display the classification for the invoice based on the
            customer. Initially blank and displayed in POST.

    """

    WAREHOUSE_LIST = [("de", "DE"), ("ch", "CH")]

    CUSTOMER_LIST = [("de", "DE"), ("ch", "CH"), ("fr", "FR"), ("us", "US")]

    TAX_RATE_DICT = {0.19: "19%", 0.077: "7.7%", 0: "Steuerfrei"}

    warehouse = models.CharField(max_length=2, choices=WAREHOUSE_LIST)
    customer = models.CharField(max_length=2, choices=CUSTOMER_LIST)
    net = models.DecimalField(
        max_digits=11, decimal_places=2, validators=[MinValueValidator(1)]
    )
    tax_rate = models.DecimalField(max_digits=4, decimal_places=3, blank=True)
    gross = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    classification = models.CharField(max_length=2, blank=True)
