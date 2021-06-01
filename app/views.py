from django.shortcuts import render, redirect
from app.api import get_rates


# Create your views here.

def rediret_index(request):
    return redirect("home",days_range=30, currencies="USD")


def dashboard(request, days_range=60, currencies="USD"):

    days, rates = get_rates(currencies=currencies.split(","), days=days_range)
    page_label={
        7:"Semaine", 30:"Mois", 365:"Année"
    }.get(days_range,"Personnalisé")
    contex = {'data': rates, 'days': days, 'page_label': page_label, 'currencies':currencies}

    return render(request, 'app/index.html', contex)
