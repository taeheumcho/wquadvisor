from django.shortcuts import render
from Common.DaishinAPI.CallMarketDataFromAPI import CallMarketDataFromAPI
from Common.Calendar.Period import Period
import datetime
indexPriceData = CallMarketDataFromAPI(["U001"]).callDataOnPeriod(Period('19900101',datetime.date.today().strftime("%Y%M%d")), targetField = (0,2,3,4,5,9))
print(indexPriceData["U001"])

indexPriceData2 = CallMarketDataFromAPI(["U001"]).callDataOnPeriod(Period('19900101',datetime.date.today().strftime("%Y%M%d")), targetField = (0,2,3,4,5,9))
print(indexPriceData2["U001"])