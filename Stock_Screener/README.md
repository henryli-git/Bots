# Stock Screener

This script will create a list of ticker symbols that match your stock screening criteria.    

## Instructions:

### Step 1
Ensure you have the pandas and yfinance modules installed.  Please click [here](https://pypi.org/project/yfinance/) if want more information on installing and using the yfinance module.

### Step 2
I have provided an Excel file with all the current tickers on the TSX, but you can prepare an Excel file with a column of tickers (column should be named "Ticker") for the script to screen.  The file can be in csv format, but use the pandas.read_csv() method instead

### Step 3
Input your desired criteria in the stock.info() method in the script.  All stock information is retrieved from Yahoo Finance.  If you want to see some possible screen criteria to input, call the .info function. 

### Step 3
Run Stock_Screener.py.  The list of screened stocks will be saved in csv format.  Please note that this script may take a long time for execution to finish - depending on the number of stocks you want to screen.

