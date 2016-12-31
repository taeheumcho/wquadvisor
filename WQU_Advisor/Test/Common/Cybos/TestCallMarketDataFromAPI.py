'''
Created on 2016. 12. 27.

@author: thcho
'''
from Common.DaishinAPI.CallMarketDataFromAPI import CallMarketDataFromAPI
from Common.Calendar.Period import Period
codes = "KS11"

instance = CallMarketDataFromAPI([codes])
specificDateData = instance.callDataOnSpecificDate('20161225')
print(specificDateData)

perioddata = instance.callDataOnPeriod(Period('20001206', '20161226'))
print(perioddata)