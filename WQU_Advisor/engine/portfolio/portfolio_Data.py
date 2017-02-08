'''
Created on 2016. 4. 21.

@author: thCho
'''
import numpy as np


class portfolio_data():
    
    def __init__(self, date, accumulatedPnL, assetCodes, currentAssetValue, currentWeights):
        self.date = date
        self.trading_dates = [date]
        self.dayPnL = [accumulatedPnL]
        self.accumulatedPnL = accumulatedPnL
        self.currentWeights = currentWeights
        self.weight_array = [currentWeights]
        self.asset_codes = assetCodes
        weight = np.array(currentWeights)
        assetprices = np.array(currentAssetValue)
        self.portfolio_value = np.dot(assetprices, weight.T)
        
    def getBudget(self):
        return self.budget
    
    def get_pfo_value(self):
        return self.portfolio_value
    
    def get_asset_codes(self):
        return self.asset_codes
    
    def getAccumulatedPnL(self):
        return self.accumulatedPnL
    
    def getCurrentWeights(self):
        return self.currentWeights
    
    def getWeightArray(self):
        return self.weight_array
    
    def getDayPnL(self):
        return self.dayPnL
    
    def getAssetCodes(self):
        return self.asset_codes
    
    def setBudget(self, budget):
        self.budget = budget
        
    def setAccumulatePnL(self, pnl):
        self.accumulatedPnL += pnl
        self.dayPnL.append(pnl)
    
    def setAssets(self, assets):
        self.assets = assets
        
    def setWeights(self, weights):
        self.currentWeights = weights
        
    def update_portfolio_data(self, date, weight, value):
        self.weight_array.append(weight)
        self.trading_dates.append(date)
        pnl = value - self.portfolio_value
        self.dayPnL.append(pnl)
        self.accumulatedPnL += pnl
        self.currentWeights = weight
        self.portfolio_value = value
        
    def getWeight(self):
        return self.currentWeights 
        
    def update_new_data(self, date, weight):
        old_weight = np.array(self.currentWeights)
        new_weight = np.array(weight)
        self.currentWeights = weight
        weight_diff = new_weight - old_weight
        
