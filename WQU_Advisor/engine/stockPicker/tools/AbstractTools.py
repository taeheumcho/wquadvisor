'''
Created on 2016. 6. 15.

@author: thCho
'''
from abc import ABCMeta, abstractmethod


class AbstractTools(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def getAssetPoint(self):
        pass