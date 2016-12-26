from django.shortcuts import render

# Create your views here.
def marketScreen(request):
    return render(request, 'FrontModule/index.html')

def backTest(request):
    return render(request, 'FrontModule/backtest.html')
