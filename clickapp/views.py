from django.shortcuts import render
from .forms import TariffCalcForm

# Create your views here.
def index(request):
    form = TariffCalcForm
    context = {'form': form}
    return render(request, 'clickapp/index.html', context)


def result(request):
    form = TariffCalcForm(request.POST)
    context = {'form': form}
    if form.is_valid():
        return(render, 'clickapp/result.html', context)
    else:
        return render(request, 'clickapp/index.html', context)
