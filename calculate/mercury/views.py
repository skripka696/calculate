from django.shortcuts import render


def index(request):
    """
    Entry to app
    """
    return render(request, 'mercury/index.html', {'title': 'PricePoint - Pricing Tool'})
