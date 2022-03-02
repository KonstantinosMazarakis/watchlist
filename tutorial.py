# Provides ways to work with large multidimensional arrays
import numpy as np 
# Allows for further data manipulation and analysis
import pandas as pd
from pandas_datareader import data as web # Reads stock data 
import matplotlib.pyplot as plt # Plotting
import matplotlib.dates as mdates # Styling dates

import datetime as dt # For defining dates
import mplfinance as mpf # Matplotlib finance
tickers=pd.read_csv("tickers.csv")


# Function that gets a dataframe by providing a ticker and starting date
def save_to_csv_from_yahoo(ticker, syear, smonth, sday, eyear, emonth, eday,file = "single"):
    
    # Defines the time periods to use
    start = dt.datetime(syear, smonth, sday)
    end = dt.datetime(eyear, emonth, eday)
    
    # pulls single stack informations
    df = web.DataReader(ticker, 'yahoo', start, end)
    
    df.to_csv(f"C:/CodingDojo/projects/watchlist/csv/{file}/" + ticker + '.csv')
    return df




# Reads a dataframe from the CSV file, changes index to date and returns it
def get_df_from_csv(ticker,file = "single"):
    try:
        df = pd.read_csv(f"C:/CodingDojo/projects/watchlist/csv/{file}/" + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df


def coefficient_of_variation(stock):
    cov = (stock['Close'].std() / stock['Close'].mean() * 100)
    return cov

# Get ROI between 2 dates
def roi(stock):
    try:
        start_val = float(stock.tail(1)["Close"])
        end_val = float(stock.head(1)["Close"])
        roi = ((end_val - start_val) / start_val) * 100
    except Exception:
        print("Data Corrupted")
    else:
        return roi


def all_stocks(syear, smonth, sday, eyear, emonth, eday, file = "all"):
    for ticker in tickers['Symbol']:
        try:
            save_to_csv_from_yahoo(ticker, syear, smonth, sday, eyear, emonth, eday, file)
            print("Working on: " + ticker)
        except:
            pass
    return



def watchlist():
    for ticker in tickers['Symbol']:
        try:
            stock = get_df_from_csv(str(ticker), file = "all")
            cov = coefficient_of_variation(stock)
            roi = roi(stock)
            print(f"{ticker} : Cov : {cov}")
        except TypeError:
            print("File Doesn't Exist")
    return



# abt = get_df_from_csv("ABT", file = "all")
# print(coefficient_of_variation(abt))
# watchlist()

save_to_csv_from_yahoo("AAPL",2022,2,21,2022,2,25)
AAPL =get_df_from_csv("AAPL")
# print(AAPL.head(1)["Close"])
# print(AAPL.tail(1)["Close"])
print(coefficient_of_variation(AAPL))
print(roi(AAPL))