'''
Created on 2016. 12. 30.

@author: thcho
'''
import win32com.client 
inCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
print(inCpStockCode.NameToCode("KOSPI200"))