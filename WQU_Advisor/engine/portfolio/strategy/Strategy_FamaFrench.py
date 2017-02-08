'''
Created on 2016. 4. 20.

@author: thCho
'''
from abc import abstractmethod

from engine.portfolio.strategy.AbstractStrategy import AbstractStrategy
import numpy as np
import pandas as pd


class Strategy_FamaFrench(AbstractStrategy):
    def __init__(self):
        self.asset_prices = [1]
        self.weight = []
    
   
    def calculate_weights(self, date):
        trainingPeriod = 1
        
        AbstractStrategy.calculate_weights(self)