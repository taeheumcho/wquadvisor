'''
Created on 2016. 6. 8.

@author: thCho
'''

import _thread

from hmmlearn.hmm import GaussianHMM

from AIMapper.models import StockData
from engine.portfolio.strategy.AbstractStrategy import AbstractStrategy
import numpy as np


tmp_asset_price = {'money': 1.0}
class Strategy_HMM(AbstractStrategy):
    def __init__(self, assetCodes, train_startDate):
        self.asset_prices = [1]
        self.start_date = train_startDate
#         self.start_date = '20010101'
        self.asset_codes = assetCodes
        self.historical_Data = {}
        self.weight = []
        self.stacked = False
        self.tmpAssetPrice = {'money': 1.0}
        self.tradingDates = StockData.objects.values('dt').distinct()
        self.trainingDates = []
    
   
    def calculate_weights(self, date, amount):
        if self.stacked == False:
            for elements in self.tradingDates:
                if elements.get('dt') >= self.start_date and elements.get('dt') <= date :
                    self.trainingDates.append(elements['dt'])
            for assetCode in self.asset_codes:
                assetValues = []
#                 for each_date in self.trainingDates:
#                     assetValues.append(StockData.objects.filter(dt=each_date,ticker=assetCode).values("price_close")[0]['price_close'])
                assetValues = [StockData.objects.filter(dt=each_date,ticker=assetCode).values("price_close")[0]['price_close'] for each_date in self.trainingDates]    
                self.historical_Data[assetCode] = assetValues
            self.stacked = True
        else:
            assetValues = []
            for assetCode in self.asset_codes:
                self.historical_Data[assetCode].append(StockData.objects.filter(dt=date,ticker=assetCode).values("price_close")[0]['price_close'])    
        
        target = {'money': amount}    
        for assetCode in self.asset_codes:
            close_v = np.array(self.historical_Data[assetCode])
            diff = np.diff(close_v)
            X = np.column_stack([diff])
            model = GaussianHMM(n_components=2, covariance_type="diag", n_iter=1000).fit(X)
            hidden_states = model.predict(X)
            stableProb = 0
            if hidden_states[len(hidden_states) - 1] == 1:
                stableProb = model.transmat_[1][1]
            else:
                stableProb = 0
            target[assetCode] = stableProb
            target['money'] -= stableProb * close_v[len(close_v) - 1]
            
        self.weight = []
        self.weight.append(target['money'])
#         for assetCode in self.asset_codes:
#             self.weight.append(target[assetCode])
        self.weight += [target[assetCode] for assetCode in self.asset_codes]    
        return self.weight
            
# def get_asset_price(date, assetCode):
#     tmpAssetPrice[assetCode] = StockData.objects.filter(TICKER=assetCode, DT=date)).values("PRICE_CLOSE")
    