from exception import CustomException
import sys
import pandas as pd

def main():
    try:
        pd.read_csv("da.csv")
    except Exception as e:
        raise CustomException(e,sys.exc_info())

if __name__ == "__main__":
    main()