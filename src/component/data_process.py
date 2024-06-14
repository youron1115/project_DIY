from sklearn.preprocessing import StandardScaler,OneHotEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
import sys

class data_split_and_output:
    #def __init__(self, data, target, test_size=0.2):
    def __init__(self, data, target, test_size=0.2):
        self.data = data
        self.target = target
        self.test_size = test_size
        logging.info("Data split :\nData column : {}\nTest size : {}".format(self.data.columns, self.test_size))
        #logging.info("Data split  Test size : {},random_state is set".format(self.test_size))
    
    def split(self):
        X_train, X_test, y_train, y_test = train_test_split(self.data, self.target, test_size=self.test_size, random_state=42)
        logging.info("Data split done")
        
        return X_train, X_test, y_train, y_test
     
class data_preprocess:
    def __init__(self, data,scalar):
        self.data=data
        self.scalar=scalar
        
    def num_process(self):
        logging.info("Numerical data preprocessing: ")
        self.data = self.scalar.fit_transform(self.data)
        return self.data
        
    def cat_process(self,scalar=OneHotEncoder(sparse_output=False)):
        logging.info("Categorical data preprocessing ")
        self.data = self.scalar.fit_transform(self.data)
        return self.data, self.scalar.get_feature_names_out()

    
    