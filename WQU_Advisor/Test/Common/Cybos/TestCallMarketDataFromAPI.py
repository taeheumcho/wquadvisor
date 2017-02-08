'''
Created on 2016. 12. 27.

@author: thcho
'''
from Common.DaishinAPI.CallMarketDataFromAPI import CallMarketDataFromAPI
from Common.Calendar.Period import Period
import datetime
import json
codes = "U001"

instance = CallMarketDataFromAPI([codes])
# specificDateData = instance.callDataOnSpecificDate('20161225')
# print(specificDateData)


perioddata = instance.callDataOnPeriod(Period('20001206', '20161226'),code="U001",targetField = (0,2,3,4,5,9))
indexPriceJason = json.dumps(perioddata["U001"])

# print(indexPriceJason)
# print(len(indexPriceJason))
# print(indexPriceJason[0][0])

# today = datetime.date.today()
# print(today)
# 
# periodAmountData = instance.callTradingVolumeByInstitutions(Period('20001206', '20170104'), marketCode = ord('B'), investorCode = '1')
# print(periodAmountData)

