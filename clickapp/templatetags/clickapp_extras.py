"""
Provide template tags for clickapp.
"""

from django import template
from django.utils.encoding import force_text

register = template.Library()


@register.filter
def intdot(value):
    """
    Similar to 'django.contrib.humanize.intcomma', but with dots.
    """
    val_text = force_text(value)
    val_int = val_text[:-3]
    val_decimal = val_text[-3:]
    try:
        val_new = int(val_int)
    except ValueError:
        return "------"

    val_new = "{:,d}".format(val_new)
    val_new = val_new.replace(",", ".")
    val_decimal = val_decimal.replace(".", ",")
    val_new += val_decimal
    return val_new
