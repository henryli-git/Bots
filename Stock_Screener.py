import pandas as pd
import yfinance as yf
import pickle as pkl

df = pd.read_excel('tsx_stocks_2020.xlsx')                         # Other files with ticker symbols can be inputed here
tickers = df['Ticker'].values.tolist()

stock_list = []
for i in tickers[:20]:
    stock = yf.Ticker(i)
    try:                                                               # Additional screening criteria can be added here
        if stock.info['pegRatio'] < 3:
            if stock.info['priceToBook'] < 1:
                if stock.info['priceToSalesTrailing12Months'] < 2:
                    stock_list.append(i)
    except:
        pass

with open('stock_list.pkl', 'wb') as file:                   # List of screened stocks can be saved in other formats here
    pkl.dump(stock_list, file)
