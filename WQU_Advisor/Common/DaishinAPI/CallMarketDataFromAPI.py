'''
Created on 2016. 12. 23.

@author: thcho
'''
import win32com.client
from Common.Calendar.Period import Period
 
# 0: 날짜(ulong)
# 1:시간(long) - hhmm
# 2:시가(long or float)
# 3:고가(long or float)
# 4:저가(long or float)
# 5:종가(long or float)
# 6:전일대비(long or float) - 주) 대비부호(37)과 반드시 같이 요청해야 함
# 8:거래량(ulong or ulonglong) 주) 정밀도 만원 단위
# 9:거래대금(ulonglong)
# 10:누적체결매도수량(ulong or ulonglong) - 호가비교방식 누적체결매도수량
# 11:누적체결매수수량(ulong or ulonglong) - 호가비교방식 누적체결매수수량
#  (주) 10, 11 필드는 분,틱 요청일 때만 제공
# 12:상장주식수(ulonglong)
# 13:시가총액(ulonglong)
# 14:외국인주문한도수량(ulong)
# 15:외국인주문가능수량(ulong)
# 16:외국인현보유수량(ulong)
# 17:외국인현보유비율(float)
# 18:수정주가일자(ulong) - YYYYMMDD
# 19:수정주가비율(float)
# 20:기관순매수(long)
# 21:기관누적순매수(long)
# 22:등락주선(long)
# 23:등락비율(float)
# 24:예탁금(ulonglong)
# 25:주식회전율(float)
# 26:거래성립률(float)
# 37:대비부호(char) - 수신값은 GetHeaderValue 8 대비부호와 동일
class CallMarketDataFromAPI():
    def __init__(self, codes):
        self.assetCodes = codes
        
    def callDataOnPeriod(self, period, code = None, targetField = (5), dataType = 'D'):
        assetPrices = {}
        if(code == None):
            for codeIdx in range(0, len(self.assetCodes)):
                inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
                inStockChart.SetInputValue(0, self.assetCodes[codeIdx])        # 대신증권 코드
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
                    assetPrices[self.assetCodes[codeIdx]] = [inStockChart.GetDataValue(0, num-1-idx) for idx in range(num)]   
        else:
            inStockChart = win32com.client.Dispatch("CpSysdib.StockChart")
            inStockChart.SetInputValue(0, code)        # 대신증권 코드
            inStockChart.SetInputValue(1, ord('1'))
            inStockChart.SetInputValue(2, period.getEndDate())
            inStockChart.SetInputValue(3, period.getStartDate())
            inStockChart.SetInputValue(5, 5)
            inStockChart.SetInputValue(6, ord(dataType))
            inStockChart.SetInputValue(9, '1')
            inStockChart.BlockRequest() 
            num = inStockChart.GetHeaderValue(3)
            if(num == 0):
                assetPrices[code] = []
            else:
                assetPrices[code] = [inStockChart.GetDataValue(0, num - idx - 1) for idx in range(num)]
        
        return assetPrices
                
    def callDataOnSpecificDate(self, date, code = None, targetField = (5), dataType = 'D'):
        return self.callDataOnPeriod(Period(date,date), code, targetField, dataType)
    
        
