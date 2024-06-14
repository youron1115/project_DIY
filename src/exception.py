import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    print("error_detail:",error_detail)
    _,_,exc_tb=error_detail
    #error_detail.exc_info()返回:類型、值和追蹤信息
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="\nError occured in python script name: {0}\nline number: {1}\nerror message: {2}".format(
    file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        logging.error(self.error_message)
    def __str__(self):
        return self.error_message