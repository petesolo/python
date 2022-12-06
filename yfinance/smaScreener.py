import pandas as pd
import yfinance as yf

stocksCSV = 'https://datahub.io/core/s-and-p-500-companies/r/constituents.csv'
spxStocks = pd.read_csv(stocksCSV)
primeList = pd.DataFrame(columns=['Stock','Current Price','YTD High','YTD Low','Current Volume','Average Volume','Six Month Return','Twelve Month Return'])

print('Retrieving SPX Index data...')
spxIndex = yf.Ticker('^GSPC')
spxIndexData = spxIndex.history(start='1900-01-01', interval='1d')
spxPriceLast = spxIndexData['Close'][-1]
spxPrice26wk = spxIndexData['Close'][-130]
spxPrice52wk = spxIndexData['Close'][-260]
spxStr26wk = (spxPriceLast - spxPrice26wk) / spxPrice26wk
spxStr52wk = (spxPriceLast - spxPrice52wk) / spxPrice52wk
print()

for ticker in spxStocks['Symbol']:
    print('Now checking stock ' + str(ticker))
    ticker = ticker.replace('.','-')
    try:
        stock = yf.Ticker(ticker)
        stockData = stock.history(start='1923-01-01', interval='1d')
        smasUsed = [21,50,100,200]
        for sma in smasUsed:
            stockData['SMA_' + str(sma)] = stockData['Close'].rolling(window=sma).mean()
        currClose = stockData['Close'][-1]
        price26wk = stockData['Close'][-130]
        price52wk = stockData['Close'][-260]
        currVol = stockData['Volume'][-1]
        sma21 = stockData['SMA_21'][-1]
        sma50 = stockData['SMA_50'][-1]
        sma100 = stockData['SMA_100'][-1]
        sma200 = stockData['SMA_200'][-1]
        avgVol = stockData['Volume'][-65:].mean()
        low52wk = min(stockData['Close'][-260:])
        high52wk = max(stockData['Close'][-260:])
        stockStr26wk = (currClose - price26wk) / price26wk
        stockStr52wk = (currClose - price52wk) / price52wk
        stockData['Signal'] = 0.0
        # Conditions to scan for:
        if currClose > sma21 and currClose > sma50 and currClose > sma100 and currClose > sma200:
            priceForce = True
        else:
            priceForce = False
        if currVol > avgVol:
            volForce = True
        else:
            volForce = False
        if sma50 > sma100 and sma100 > sma200:
            smaForce = True
        else:
            smaForce = False
        if stockStr26wk > spxStr26wk and stockStr52wk > spxStr52wk:
            marketForce = True
        else:
            marketForce = False
        # Consolidate all conditions
        if priceForce and volForce and smaForce and marketForce:
            scanData = {
                'Stock': ticker,
                'Current Price': currClose,
                'YTD High': high52wk,
                'YTD Low':low52wk,
                'Current Volume': currVol,
                'Average Volume': avgVol,
                'Six Month Return': stockStr26wk,
                'Twelve Month Return': stockStr52wk,
            }
            primeList = pd.concat([primeList, pd.DataFrame([scanData])], ignore_index=True)
        else:
            continue
    except:
        print('No data on ' + str(ticker))
        continue
# Export DataFrames to .CSV Files
primeList.to_csv('primeSelected.csv',index=False)
print('Prime List: ')
print(primeList)
print()