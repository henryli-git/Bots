import pandas as pd
import yfinance as yf

df = pd.read_excel('tsx_stocks_2020.xlsx')                         # Other files with ticker symbols can be inputed here
tickers = df['Ticker'].values.tolist()

stock_list = []
for i in tickers[:20]:
    stock = yf.Ticker(i)
    try:                                                               # Additional screening criteria can be added here
        if stock.info['pegRatio'] < 300:
            if stock.info['priceToBook'] < 100:
                if stock.info['priceToSalesTrailing12Months'] < 200:
                    stock_list.append(i)
    except:
        pass

df2 = pd.DataFrame(stock_list, columns=['Tickers'])
df2.to_csv('stock_list.csv', index=False)        # Screened stocks will be saved in csv format - change save format here
