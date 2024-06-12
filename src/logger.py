import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
#檔案名稱:如2021-09-01-12-30-45.log

dir=r"D:\project_DIY\\logs"

os.makedirs(dir,exist_ok=True)
"""
當exist_ok設置為True時，
如果目標目錄已存在，函數將不會拋出FileExistsError異常
反之，如果exist_ok設置為False（默認值），
當目標目錄已存在時，將會拋出FileExistsError異常
"""

logs_path=os.path.join(dir,LOG_FILE)
#logs_path為目前工作資料夾下建立logs資料夾，並在logs資料夾下建立LOG_FILE檔案


logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #紀錄時間,行數,名稱,等級,訊息
    level=logging.DEBUG,
)
