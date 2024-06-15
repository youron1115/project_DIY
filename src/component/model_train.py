import pandas as pd
import numpy as np
from datetime import datetime
import joblib
import os
import sys

from sklearn.ensemble import (
    RandomForestClassifier,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR, SVC

from src.exception import CustomException
from src.logger import logging

class model_build:
    def __init__(self, model, X_train, y_train, X_test, y_test):
        
        self.model=model
        
        self.X_train=X_train
        self.y_train=y_train
        self.X_test=X_test
        self.y_test=y_test
        
        logging.info("Model building started for model : {}".format(self.model))
        
    def fit_model(self):
        #創建一個模型來擬合訓練數據
        try:
            self.model.fit(self.X_train, self.y_train)
            logging.info("Model fitting done")
            return self.model
        except Exception as e:
            raise CustomException(e,sys.exc_info())
    
    def predict_model(self):
        #對測試集進行預測
        try:
            y_pred = self.model.predict(self.X_test)
            logging.info("Model prediction done")
            return y_pred
        except Exception as e:
            raise CustomException(e,sys.exc_info())
    
    def evaluate_model(self):
        #評估模型
        try:
            logging.info("Model evaluation returned")
            return self.model.score(self.X_test, self.y_test)
        except Exception as e:
            raise CustomException(e,sys.exc_info())

class choose_model:
    def __init__(self,X_train, y_train, X_test, y_test):
        self.model_save_path=None
        self.X_train=X_train
        self.y_train=y_train
        self.X_test=X_test
        self.y_test=y_test
        
        
        self.model= {"tree":{
                "Random Forest classifier": RandomForestClassifier(),
                "Decision Tree": DecisionTreeClassifier(),
                },
                     "linear":{
                #"linear regression":LinearRegression(),
                #"logistic regression":LogisticRegression(),
                },
                     "svm":{
                #"SVR":SVR(),
                #"SVC":SVC()
                }
            }
        
    def save_model(self,model,model_name):
        try:
            model_name=f"{model_name}.joblib"
            model_save_path="D:\project_DIY\model"+"/"+model_name
            model_save_path=model_save_path.replace("\\","/")
            joblib.dump(model, model_save_path)
            logging.info("Model saved : {}\n".format(model_save_path))
        except Exception as e:
            raise CustomException(e,sys.exc_info())
      
    def train_model(self):
        try:
            score_dict=dict()
            model_name_dcit=dict()
            logging.info("Model training list started\n")
            for model_type in self.model.keys():
                for model_name in self.model[model_type].keys():
                    logging.info("Model name : {}".format(model_name))
                    model=self.model[model_type][model_name]
                    model_building=model_build(model,self.X_train, self.y_train, self.X_test, self.y_test)
                    model=model_building.fit_model()
                    score=model_building.evaluate_model()
                    
                    score_dict[model_name]=score
                    model_name_dcit[model_name]=model
                    
                    logging.info("Model score : {}\n".format(score))
                    
            logging.info("Model training list done\nscore:{}".format(score_dict))
            best_model_name=max(score_dict, key=lambda x: np.max(score_dict[x]))

            if score_dict[best_model_name]<0.6:
                logging.info("No best model > 0.6 found")
            
            
            
            logging.info("choose model :{}".format(model_name_dcit[best_model_name]))

            logging.info("Model training done\n")
            return best_model_name,model_name_dcit[best_model_name]
                    
        except Exception as e:
            raise CustomException(e,sys.exc_info())
    