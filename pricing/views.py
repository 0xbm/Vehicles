from django.shortcuts import render


# Create your views here.

def pricing(request):
    return render(request, 'pricing/index.html')


def pay_3(request):
    return render(request, 'pay/pay_3.html')


def pay_6(request):
    return render(request, 'pay/pay_6.html')


def pay_9(request):
    return render(request, 'pay/pay_9.html')


def pay_12(request):
    return render(request, 'pay/pay_12.html')
