from django.forms import modelformset_factory
from django.shortcuts import render
from .forms import TariffCalcForm
from .models import TariffCalc


def index(request):
    """
    Display model form as formset
    """

    if request.method == "POST":
        TCFormset = modelformset_factory(TariffCalc, form=TariffCalcForm)
        formset = TCFormset(request.POST)
        context = {"formset": formset}

        for form in formset:
            if form.is_valid():
                return render(request, "clickapp/index.html", context)

    TCFormset = modelformset_factory(TariffCalc, form=TariffCalcForm, extra=9)
    formset = TCFormset()
    context = {"formset": formset}
    return render(request, "clickapp/index.html", context)
