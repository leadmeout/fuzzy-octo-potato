from django.forms import ModelForm
from .models import TariffCalc
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class TariffCalcForm(ModelForm):
    """
    Define Tariff Calculator model form object
    """

    class Meta:
        model = TariffCalc
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_show_labels = False
        self.helper.add_input(Submit("submit", "Calculate"))

    CLASSIFICATION_DICT = {"ch": "EU", "de": "EU", "fr": "EU", "us": "US"}

    INTERNAL_TAX_DICT = {
        "de": 0.19,
        "ch": 0.077,
        "us": 0,
    }

    TAX_RATE_DICT = {0.19: "19%", 0.077: "7.7%", 0: "Steuerfrei"}

    @property
    def get_tax_rate(self):
        """
        Returns the tax rate to be displayed on the results page
        """

        try:
            warehouse = self.cleaned_data["warehouse"]
            customer = self.cleaned_data["customer"]
        except KeyError:
            return "------"
        except AttributeError:
            return "------"

        if customer:
            try:
                tax = self.INTERNAL_TAX_DICT[customer]
            except KeyError:
                if warehouse:
                    tax = self.INTERNAL_TAX_DICT[warehouse]

            return self.TAX_RATE_DICT[tax]

        return "------"

    @property
    def get_gross(self):
        """
        Returns the gross total to be displayed on the results page.
        """

        try:
            receiver = self.cleaned_data["customer"]
            net_total = float(self.cleaned_data["net"])
        except KeyError:
            return "------"
        except AttributeError:
            return "------"

        if receiver and net_total:
            try:
                tax = float(self.INTERNAL_TAX_DICT[receiver])
            except KeyError:
                tax = float(self.INTERNAL_TAX_DICT[self.cleaned_data["warehouse"]])
            gross_total = round(net_total * tax + net_total, 2)
            return f"{gross_total:.2f}"

        return "------"

    @property
    def get_classification(self):
        """
        Returns classification to be displayed on results page.
        """
        try:
            receiver = self.cleaned_data["customer"]
            classification = self.CLASSIFICATION_DICT[receiver]
        except KeyError:
            return "------"
        except AttributeError:
            return "------"

        return classification
