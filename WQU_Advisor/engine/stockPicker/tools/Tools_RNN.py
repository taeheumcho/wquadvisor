'''
Created on 2016. 6. 15.

@author: thCho
'''
import math

from AIMapper.models import StockData
from engine.stockPicker.tools.AbstractTools import AbstractTools
import keras.callbacks
from keras.layers.core import Dense, Activation, Dense, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential  
import numpy as np

class Tools_RNN(AbstractTools):
    def __init__(self, assetCode, trainstartDate):
        self.asset_code = assetCode
#         self.train_asset_codes = train_assets
        self.historical_Data = {}
        self.stacked = False
        self.tradingDates = StockData.objects.values('dt').distinct()
        self.trainingDates = []
        self.train_start = trainstartDate
        self.time_lag = 1
    
    def getAssetPoint(self, date):
# step1. clean data arrays (1. training dates, 2. stock price -> return, 3. output -> {0,1}
#        a. training Dates
       
        if self.trainingDates == [] :
            for elements in self.tradingDates:
                if elements.get('dt') >= self.train_start and elements.get('dt') <= date :
                    self.trainingDates.append(elements['dt'])
        else:
            if date in self.tradingDates and date not in self.trainingDates:
                self.trainingDates.append(date)
        
        self.historical_Data = [StockData.objects.filter(dt=dateElement, ticker=self.asset_code).values("price_close")[0]['price_close'] for dateElement in self.trainingDates]
        returnData = [math.log(self.historical_Data[i + 1] / self.historical_Data[i]) for i in range(0,len(self.historical_Data) - self.time_lag)] 
        outputData = [ (lambda x: x >0 and 1 or 0)(x) for x in returnData ]
        inputX = np.array(returnData)
        outputY = np.array(outputData)
        input_mat = np.array([[x] for x in inputX])
#         np.concatenate(inputX, axis=0)
        target_mat =outputY 
#         np.concatenate(outputY, axis=0)
        trials = input_mat.shape[0]
        features = input_mat.shape[1]
        hidden = 2
        model = Sequential()
        model.add(LSTM(hidden, input_shape=(len(self.historical_Data), features)))
#         model.add(Dropout(.2))
        model.add(Dense(self.time_lag))
        model.add(Activation('linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        history = LossHistory()
        model.fit(input_mat, target_mat, nb_epoch=100, batch_size=400, callbacks=[history])
        pass
        
# Call back to capture losses 
class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []

    def on_batch_end(self, batch, logs={}):
        self.losses.append(logs.get('loss'))