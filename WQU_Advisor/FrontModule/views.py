#-*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http.response import JsonResponse
from Common.DaishinAPI.CallMarketDataFromAPI import CallMarketDataFromAPI
from Common.Calendar.Period import Period
import datetime
import json

# Create your views here.
def marketScreen(request):
    return render(request, 'FrontModule/home.html',{})


def chart_data_json(request):
    tmpclass = CallMarketDataFromAPI(["U001"])
    indexPriceDatas = tmpclass.callDataOnPeriod(Period('20100101','20161226'), code = "U001", targetField = (0,2,3,4,5,9))
#     datetime.date.today().strftime("%Y%M%d")
    indexPriceJason = json.dumps(indexPriceDatas["U001"])
#     print(indexPriceJason)
    tmpclass = None
    return JsonResponse(indexPriceDatas["U001"], safe=False)
    
def backTest(request):
    
    return render(request, 'FrontModule/backtest.html')
