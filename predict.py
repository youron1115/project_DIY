# 1. 導入必要的庫

import pandas as pd
from src.logger import logging
from src.exception import CustomException
import sys
import joblib

from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

# 2. 加載iris數據集
df=pd.read_csv(r"D:\Code-repo\平板購買預測決策樹\train_data.csv")

from src.component import data_process
from src.component import model_train


try:

    num,cat=df[['rate','income_per_month']],df[['subject']]
    
    num_process=data_process.data_preprocess(num,StandardScaler())
    num=num_process.num_process()
    
    cat_process=data_process.data_preprocess(cat,OneHotEncoder(sparse_output=False))
    cat,cat_col=cat_process.cat_process()
    
    num=pd.DataFrame(num,columns=['rate','income_per_month'])
    cat=pd.DataFrame(cat,columns=cat_col)
    X=pd.concat([num,cat],axis=1)

    y=cat
    
    split_1=data_process.data_split_and_output(X,y,0.3)
    X_train,X_test,y_train,y_test=split_1.split()
    
    split_2=data_process.data_split_and_output(X_train,y_train)
    X_train,X_valid,y_train,y_valid=split_2.split()
    
    #y_train_path=r"D:\project_DIY\artifact\y_train.csv"
    #y_test_path=r"D:\project_DIY\artifact\y_test.csv"
    
    #y_train.to_csv(y_train_path,index=False)
    #y_test.to_csv(y_test_path,index=False)
    
    
    #y_train=pd.read_csv(r"D:\project_DIY\src\component\data\y_train.csv")
    #y_test=pd.read_csv(r"D:\project_DIY\src\component\data\y_test.csv")
    
    
    c=model_train.choose_model(X_train, y_train, X_valid, y_valid)
    name,dicts=c.train_model()
    
    DT=DecisionTreeClassifier(random_state=0)
    
    DT.fit(X_train,y_train)
    
    pred=DT.predict(X_test)
    #print("pred:",pred)
    logging.info("model evaluate success:{}".format(DT.score(X_valid,y_valid)))
    logging.info("model test success:{}".format(DT.score(X_test,y_test)))

except Exception as e:
    raise CustomException(e,sys.exc_info())