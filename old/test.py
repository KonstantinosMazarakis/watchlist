
import yfinance as yf
import pandas as csv

# stock = yf.Ticker("MSFT")
# print(stock.history(period="2d"))

# list all stocks
tickers=csv.read_csv("tickers.csv")


movementlist = []
for ticker in tickers['Symbol']:
    try:
        stock = yf.Ticker(ticker)
        stock_history = stock.history(period="2d")
        day1_volume = stock_history["Volume"].values[0]
        day2_volume = stock_history["Volume"].values[1]
        if ((day1_volume - day2_volume) / day2_volume ) * 100 >= 20:
            print(f"{ticker}: Has a greater than 20 percent increase")
        else:
            print(f'{ticker}: HasNot enough increase')
    except IndexError:
        print("No Data Found")















    # day1 = stock_history.iloc[[0]]
    # day2 = stock_history.iloc[[1]]
    # for i  in day1.itertuples(index=True, name='Pandas'):
    #     print(i.Volume)
    # if day1.Volume == 0:
    #     print("fail")

    # days = stock_history.itertuples(index=True, name='Pandas')

        # if day.High >  (day.High * 1.2):
        #     print("Greater than 20 percent increase")
        # else:
        #     print('Not enough increase')
