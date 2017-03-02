'''
Created on 2017. 2. 17.

@author: thcho
'''
import win32com.client 
inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
inCpCodeMgr = win32com.client.Dispatch("CpUtil.CpCodeMgr")

totalNumber = inCpStockCode.GetCount()
print(totalNumber)
for i in range(totalNumber):
    info = []
    type = inCpCodeMgr.GetStockMarketKind(inCpStockCode.GetData(0,i))
    type2 = inCpCodeMgr.GetStockSectionKind(inCpStockCode.GetData(0,i))
    if (type == 1 or type == 2) and type2 == 1:
        typestring = ""
        if type == 1:
            typestring = "KOSPI"
        else:
            typestring = "KOSDAQ"    
        info.append(inCpStockCode.GetData(0,i))
        info.append(inCpStockCode.GetData(1,i))
        info.append(inCpStockCode.GetData(2,i))
        info.append(typestring)
        print(info)  # 0~9번에 대한 종목 코드를 리턴
        print(type2)
        
    
    
    