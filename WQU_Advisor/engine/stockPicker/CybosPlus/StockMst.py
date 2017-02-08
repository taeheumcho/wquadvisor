'''
Created on 2016. 7. 31.

@author: Jay
'''
import win32com.client

class StockMstClass(object):
    '''
    StockMst
    '''
    class InputType(enumerate):
        StockCode = 0
    
    class OutputType(enumerate):
        StockCode = 0
        StockName = 1
        DaiShinCode = 2
        GroupCode = 3
        Time = 4
        Gubun = 5
        Size = 6
        UpperPrice = 8
        LowerPrice = 9
        PrevClosePrice = 10
        CurrentPrice = 11
        NetChange = 12
        OpenPrice = 13
        HighestPrice = 14
        LowestPrice = 15
        AskPrice = 16
        BidPrice = 17
        CumulativeVolume = 18
        CumulativeAmount = 19
        EPS = 20
        RecordHighPrice = 21
        DayOfRecordHighPrice = 22
        RecordLowPrice = 23
        DayOfRecordLowPrice = 24
        PER = 28
        ListedAmount = 31
        ForeignLimitAmount = 37
        ForeignLimitPercent = 38
        StatusCode = 44
        PreviousDayVolume = 46
        HighestPrice52wk = 47
        DayOfHighestPrice52wk = 48
        LowestPrice52wk = 49
        DayOfLowestPrice52wk = 50
        CreditBalancePercent = 64
        
    def __init__(self):
        '''
        Constructor
        '''
        self.instStockMst = win32com.client.Dispatch("dscbo1.StockMst")
    
    def setInputValue(self, inputType, value):
        self.instStockMst.SetInputValue(inputType, value)
        self.instStockMst.BlockRequest()
    
    def getResult(self, outputType):
        return self.instStockMst.GetHeaderValue(outputType)
    
    