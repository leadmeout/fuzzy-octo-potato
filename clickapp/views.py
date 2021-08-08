from django.shortcuts import render
from .forms import TariffCalcForm
from django.forms import modelformset_factory
from .models import TariffCalc


def index(request):

    TariffCalcFormSet = modelformset_factory(TariffCalc, form=TariffCalcForm, extra=9)
    formset = TariffCalcFormSet()
    context = {'formset': formset}
    return render(request, 'clickapp/index.html', context)


def result(request):

    TariffCalcFormSet = modelformset_factory(TariffCalc, form=TariffCalcForm)
    formset = TariffCalcFormSet(request.POST)
    context = {'formset': formset}

    for form in formset:
        if form.is_valid():
            return render(request, 'clickapp/result.html', context)
        else:
            return render(request, 'clickapp/index.html', context)
