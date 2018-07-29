'''
Author: James Chan
Date: 7/29/18
'''
import pandas as pd

def get_data(ticker, dates):
    df = pd.DataFrame(index=dates)
    df_tmp = pd.read_csv('QQQ.csv', index_col='Date',
            parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    df = df.join(df_tmp)
    return df
