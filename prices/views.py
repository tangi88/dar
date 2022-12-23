from django.shortcuts import render


def prices(request):
    return render(request, 'prices/prices.html')

