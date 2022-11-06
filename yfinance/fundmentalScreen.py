import pandas as pd
import yfinance as yf

ticker = 'AAPL'
stock = yf.Ticker(ticker)

stockData = stock.info
stockPNL = stock.financials
stockBS =  stock.balancesheet
stockCF = stock.cashflow

stockDataFrame = pd.DataFrame([stockData])

print(stockData)
print(stockPNL)
print(stockBS)
print(stockCF)
print(stockDataFrame)

stockDataFrame.to_csv('stockdataframe_test.csv', index=False)