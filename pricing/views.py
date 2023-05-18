from django.shortcuts import render


# Create your views here.

def pricing(request):
    return render(request, 'pricing/index.html')


def pay(request):
    return render(request, 'pay/index.html')
