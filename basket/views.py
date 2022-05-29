from django.shortcuts import render

# from .models import


def basket_summary(request):
    return render(request, "store/basket/summary.html")
