# coding=utf-8
'''
Created on 2016. 12. 23.

@author: thcho
'''

from Common.Calendar.Period import Period
import sys
import time
sys.coinit_flags = 0
import win32com.client
from servicemanager import CoInitializeEx
from servicemanager import CoUninitialize
from servicemanager import COINIT_MULTITHREADED
from datetime import datetime

class CallMarketDataFromAPI():
    def __init__(self, codes):
        self.assetCodes = codes
       
    def callDataOnPeriod(self, period, code = None, targetField = (5,), dataType = 'D'):
         
        assetPrices = {}
        if(code == None):
            for codeIdx in range(0, len(self.assetCodes)):
#                 pythoncom.CoInitialize()
                
                CoInitializeEx(COINIT_MULTITHREADED)
                
                inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
                inStockChart.SetInputValue(0, self.assetCodes[codeIdx])      
                inStockChart.SetInputValue(1, ord('1'))
                inStockChart.SetInputValue(2, period.getEndDate())
                inStockChart.SetInputValue(3, period.getStartDate())
                inStockChart.SetInputValue(5, targetField)
                inStockChart.SetInputValue(6, ord(dataType))
                inStockChart.SetInputValue(9, '1')
                inStockChart.BlockRequest()
               
                num = inStockChart.GetHeaderValue(3)
                if(num == 0):
                    assetPrices[self.assetCodes[codeIdx]] = []
                else:
                    if(len(targetField) == 0):
                        assetPrices[self.assetCodes[codeIdx]] = [[inStockChart.GetDataValue(0, num-1-idx) for tidx in range(len(targetField))] for idx in range(num)]
                    else:
                        assetPrices[self.assetCodes[codeIdx]] = [self.getDataValue(inStockChart, num-1-idx, len(targetField)) for idx in range(num)]
                CoUninitialize()   
        else:
#             pythoncom.CoInitialize()
            CoInitializeEx(COINIT_MULTITHREADED)
        
            inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
            inStockChart.SetInputValue(0, code)    
            inStockChart.SetInputValue(1, ord('1'))
            inStockChart.SetInputValue(2, period.getEndDate())
            inStockChart.SetInputValue(3, period.getStartDate())
            inStockChart.SetInputValue(5, targetField)
            inStockChart.SetInputValue(6, ord(dataType))
            inStockChart.SetInputValue(9, '1')
            inStockChart.BlockRequest()
            
            num = inStockChart.GetHeaderValue(3)
            
           
            if(num == 0):
                assetPrices[code] = []
            else:
                if(len(targetField) == 0):
                    assetPrices[code] = [[inStockChart.GetDataValue(0, num-1-idx) for tidx in range(len(targetField))] for idx in range(num)]
                else:
#                     assetPrices[code] = [[inStockChart.GetDataValue(tidx, num-1-idx) for tidx in range(len(targetField))] for idx in range(num)]
                    assetPrices[code] = [self.getDataValue(inStockChart, num-1-idx, len(targetField)) for idx in range(num)]
            CoUninitialize()
        return assetPrices
    
    def getDataValue(self, classobject, idx, targetLength):
        result = []
        
        dateValue_st = str(classobject.GetDataValue(0, idx))
#         print(dateValue_st)
        dateValue_second = int(1000*(datetime.strptime(dateValue_st, "%Y%m%d")-datetime(1970,1,1)).total_seconds())
#         print(datetime.strptime(dateValue_st, "%Y%m%d"))
        result.append(dateValue_second)
        for i in range(1,targetLength):
            result.append(classobject.GetDataValue(i, idx))
             
        return result
     
    def callDataOnSpecificDate(self, date, code = None, targetField = (5), dataType = 'D'):
        return self.callDataOnPeriod(Period(date,date), code, targetField, dataType)
    
        
    def callTradingVolumeByInstitutions(self, period, marketCode = ord('A'), investorCode = '0', targetField = (5)):
        volumeData = []
        
        inStockChart = win32com.client.Dispatch("CpSysdib.CpSvrNew7224")
        inStockChart.SetInputValue(0,ord('1'))
        inStockChart.SetInputValue(1,marketCode)
        inStockChart.SetInputValue(2,investorCode)
        inStockChart.SetInputValue(3,ord('1')) 
        inStockChart.SetInputValue(4,ord('2'))
        inStockChart.SetInputValue(5,'0')
        inStockChart.SetInputValue(6,period.getStartDate())
        inStockChart.SetInputValue(7,period.getEndDate())
        inStockChart.SetInputValue(8,  ord('1'))
        inStockChart.BlockRequest() 
        num = inStockChart.GetHeaderValue(5)
        if(num == 0):
            volumeData = []
        else:
            volumeData = [inStockChart.GetDataValue(10, idx) for idx in range(num)]
            while inStockChart.Continue:
                inStockChart.BlockRequest()
                numData = inStockChart.GetHeaderValue(5)
                volumeData += [inStockChart.GetDataValue(10, idx) for idx in range(numData)]
                time.sleep(1)       
        
        totalNum = len(volumeData)
        finalVolData = [volumeData[totalNum - idx - 1] for idx in range(totalNum)]
        return finalVolData