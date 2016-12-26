'''
Created on 2016. 12. 26.

@author: thcho
'''
from _datetime import date
class Period():
    def __init__(self, startDate, endDate):
        __startDate = startDate
        __endDate = endDate
    
    def getStartDate(self):
        return self.__startDate
    
    def getEndDate(self):
        return self.__endDate
    