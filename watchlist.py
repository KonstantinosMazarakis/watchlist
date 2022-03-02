import pandas as pd # Allows for further data manipulation and analysis
from pandas_datareader import data as web # Reads stock data 
import datetime as dt # For defining dates
import os
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



def save_to_csv_from_yahoo_all_stocks(syear, smonth, sday, eyear, emonth, eday, file = "all"):
    for ticker in tickers['Symbol']:
        try:
            save_to_csv_from_yahoo(ticker, syear, smonth, sday, eyear, emonth, eday, file)
            print("Working on: " + ticker)
        except:
            pass
    return




# Reads a dataframe from the CSV file, changes index to date and returns it
def get_df_from_csv(ticker,file = "single"):
    try:
        df = pd.read_csv(f"C:/CodingDojo/projects/watchlist/csv/{file}/" + ticker + '.csv')
    except FileNotFoundError:
        print("File Doesn't Exist")
    else:
        return df


def coefficient_of_variation(stock):
    cov = round((stock['Close'].std() / stock['Close'].mean() * 100),2)
    return cov


def roi(stock):
    try:
        start_val = float(stock.head(1)["Close"])
        start_val = round(start_val,2)
        end_val = float(stock.tail(1)["Close"])
        end_val = round(end_val,2)
        roi = round((((end_val - start_val) / start_val) * 100),2)
    except Exception:
        print("Data Corrupted")
    else:
        return roi


def watchlist():
    all_stacks_folder = os.scandir('C:/CodingDojo/projects/watchlist/csv/all/')
    for ticker in all_stacks_folder:
        try:
            stock = pd.read_csv(ticker)
            cov = coefficient_of_variation(stock)
            roi_results = roi(stock)
            print(f"{ticker} : Cov : {cov}      Roi : {roi_results}")
        except TypeError:
            print("File Doesn't Exist")
    return


#RUN

watchlist()

# save_to_csv_from_yahoo_all_stocks(2022,2,21,2022,2,25)


# save_to_csv_from_yahoo("AAPL",2022,2,21,2022,2,25)
# AAPL =get_df_from_csv("AAPL")
# print(coefficient_of_variation(AAPL))
# print(roi(AAPL))





#OLD WAY

# def watchlist():
#     for ticker in tickers['Symbol']:
#         try:
#             stock = get_df_from_csv(str(ticker), file = "all")
#             cov = coefficient_of_variation(stock)
#             roi_results = roi(stock)
#             print(f"{ticker} : Cov : {cov}      Roi : {roi_results}")
#         except TypeError:
#             print("File Doesn't Exist")
#     return





