'''
Created on 2016. 4. 20.

@author: thCho
'''

from abc import ABCMeta, abstractmethod


class AbstractStrategy(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def calculate_weights(self):
        pass
    
    def getAssetSQLInfo(self):
        pass