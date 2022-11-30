from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class calc_results:
    def __init__(self, y_true, y_pred, model):
        self.y_true = y_true
        self.y_pred = y_pred
        self.mape_val = self.mape()
        self.rmse_val = self.rmse()
        self.r2_val = self.r2()
        self.model = model
    
    def mape(self): 
        y_true, y_pred = np.array(self.y_true), np.array(self.y_pred)
        return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        
    def rmse(self):
        y_true, y_pred = np.array(self.y_true), np.array(self.y_pred)
        return np.sqrt(mean_squared_error(y_true, y_pred))
        
    def r2(self):
        y_true, y_pred = np.array(self.y_true), np.array(self.y_pred)
        return r2_score(y_true, y_pred)

    def calc_results_row(self):
        row = {'model' : self.model,
               'rmse':self.rmse_val,
               'r2': self.r2_val,
               'mape': self.mape_val, 
              }
        return row