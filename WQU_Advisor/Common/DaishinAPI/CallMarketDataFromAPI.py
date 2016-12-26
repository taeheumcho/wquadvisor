'''
Created on 2016. 12. 23.

@author: thcho
'''
import win32com.client
from multimethod import multimethod

class CallMarketDataFromAPI():
    def __init__(self, codes):
        self.assetCodes = codes
    @multimethod    
    def callDataOnPeriod(self, code = null, period, dataType):
        assetPrices = {}
        for codeIdx in range(0, len(self.assetCodes)):
            inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
            inStockChart.SetInputValue(0, self.assetCodes[codeIdx])        # 대신증권 코드
            inStockChart.SetInputValue(1, '1')
            inStockChart.SetInputValue(2, period[0])
            inStockChart.SetInputValue(3, period[1])
            inStockChart.SetInputValue(4, 1)
            inStockChart.SetInputValue(5, 5)
            inStockChart.SetInputValue(6, ord(dataType))
            inStockChart.SetInputValue(9, '1')
            inStockChart.BlockRequest()
            assetPrices[self.assetCodes[codeIdx]] = inStockChart.GetDataValue(5)
        return assetPrices
    
    @multimethod            
    def callDataOnSpecificDate(self, code = null, date):
        assetPrices = {}
        for codeIdx in range(0, len(self.assetCodes)):
            inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
            inStockChart.SetInputValue(0, self.assetCodes[codeIdx])        # 대신증권 코드
            inStockChart.SetInputValue(1, '1')
            inStockChart.SetInputValue(2, date)
            inStockChart.SetInputValue(3, date)
            inStockChart.SetInputValue(4, 1)
            inStockChart.SetInputValue(5, 5)
            inStockChart.SetInputValue(6, ord('D'))
            inStockChart.SetInputValue(9, '1')
            inStockChart.BlockRequest()
            assetPrices[self.assetCodes[codeIdx]] = inStockChart.GetDataValue(5)
        return assetPrices
    
    @multimethod
    def callDataOnSpecificDate(self, code, date, dataType):
        inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
        inStockChart.SetInputValue(0, code)        # 대신증권 코드
        inStockChart.SetInputValue(1, '1')
        inStockChart.SetInputValue(2, date)
        inStockChart.SetInputValue(3, date)
        inStockChart.SetInputValue(4, 1)
        inStockChart.SetInputValue(5, 5)
        inStockChart.SetInputValue(6, ord(dataType))
        inStockChart.SetInputValue(9, '1')
        inStockChart.BlockRequest()
        return inStockChart.GetDataValue(5)
    
    @multimethod    
    def callDataOnPeriod(self, code, period, dataType):
        inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
        inStockChart.SetInputValue(0, code)        # 대신증권 코드
        inStockChart.SetInputValue(1, '1')
        inStockChart.SetInputValue(2, period[0])
        inStockChart.SetInputValue(3, period[1])
        inStockChart.SetInputValue(4, 1)
        inStockChart.SetInputValue(5, 5)
        inStockChart.SetInputValue(6, ord(dataType))
        inStockChart.SetInputValue(9, '1')
        inStockChart.BlockRequest() 
        return inStockChart.GetDataValue(5)
        
