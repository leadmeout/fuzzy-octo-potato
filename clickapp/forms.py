from django.forms import ModelForm
from .models import TariffCalc
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class TariffCalcForm(ModelForm):
    class Meta:
        model = TariffCalc
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.add_input(Submit('submit', 'Calculate'))

        self.fields['tax_rate'].widget.attrs['readonly']=True
        self.fields['gross'].widget.attrs['readonly']=True
        self.fields['classification'].widget.attrs['readonly']=True
