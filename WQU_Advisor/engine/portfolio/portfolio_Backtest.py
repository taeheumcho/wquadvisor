'''
Created on 2016. 4. 20.

@author: thCho
'''
from multiprocessing.pool import ThreadPool as Pool

from AIMapper.models import StockData
import numpy as np


class portfolio(object):
    
    def __init__(self, portfolio_data, strategy):
        self.assetCodes = portfolio_data.get_asset_codes()
        self.strategy = strategy
        self.weight_array = [portfolio_data.getCurrentWeights()]
        self.tradingDates = StockData.objects.values('dt').distinct()
        self.portfolio = portfolio_data
    
    def backTest(self, testPeriod):
        weight_at_time = []
        weight_timearray = [[]]
        testDates = []
        pool_size = 4
        pool = Pool(pool_size)
       
        for elements in self.tradingDates:
            if elements.get('dt') >= testPeriod[0] and elements.get('dt') <= testPeriod[1] :
                testDates.append(elements['dt'])
        
        for dateElement in testDates:
            previous_weight = self.portfolio.getCurrentWeights()
            assetPrices = [StockData.objects.filter(dt=dateElement, ticker=assetCode).values("price_close")[0]['price_close'] for assetCode in self.assetCodes]   
            asset_value_array = [1] + assetPrices
            currentValue = np.dot(np.array(asset_value_array), np.array(previous_weight).T)
            weight = self.strategy.calculate_weights(dateElement, currentValue)
            self.portfolio.update_portfolio_data(dateElement, weight, currentValue)
            
    def get_weight_array(self):
        return self.portfolio.getWeightArray()
    
    def get_current_weight(self):
        return self.portfolio.getCurrentWeights()
    
    def get_day_PnL(self):
        return self.portfolio.getDayPnL()
            
    def get_accumulated_PnL(self):
        return self.portfolio.getAccumulatedPnL()
