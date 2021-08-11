from django.forms import modelformset_factory
from django.shortcuts import render
from .forms import TariffCalcForm
from .models import TariffCalc


def index(request):
    """
    Displays the model form as a formset on the site.

    If the request is POST, iterate through each form in the post and return
    it on the same page. Otherwise, load the blank formset with 10 rows.

    TCFormset (FormSet): Returns a FormSet object for the TariffCalc model.
    Uses the TariffCalcForm as a starting point.
    """

    if request.method == "POST":
        TCFormset = modelformset_factory(TariffCalc, form=TariffCalcForm)
        formset = TCFormset(request.POST)
        context = {"formset": formset}

        for form in formset:
            if form.is_valid():
                return render(request, "clickapp/index.html", context)

    TCFormset = modelformset_factory(TariffCalc, form=TariffCalcForm, extra=10)
    formset = TCFormset()
    context = {"formset": formset}
    return render(request, "clickapp/index.html", context)
