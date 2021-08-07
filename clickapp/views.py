from django.shortcuts import render
from .forms import TariffCalcForm

# Create your views here.
def index(request):
    form = TariffCalcForm
    context = {'form': form}
    return render(request, 'clickapp/index.html', context)
