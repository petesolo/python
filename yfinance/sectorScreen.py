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

print('Retrieving Energy sector data...')
energySector = yf.Ticker('^GSPE')
energySectorData = energySector.history(start='1900-01-01', interval='1d')
energyPriceLast = energySectorData['Close'][-1]
energyPrice26wk = energySectorData['Close'][-130]
energyPrice52wk = energySectorData['Close'][-260]
energyStr26wk = (energyPriceLast - energyPrice26wk) / energyPrice26wk
energyStr52wk = (energyPriceLast - energyPrice52wk) / energyPrice52wk
print()

print('Retrieving sector data...')
energySector = yf.Ticker('^GSPE')
materialsSector = yf.Ticker('^SP500-15')
industrialSector = yf.Ticker('^SP500-20')
discretionarySector = yf.Ticker('^SP500-25')
stapesSector = yf.Ticker('^SP500-30')
healthSector = yf.Ticker('^SP500-35')
financialSector = yf.Ticker('^SP500-40')
infoTechSector = yf.Ticker('^SP500-45')
telecommsSector = yf.Ticker('^SP500-50')
utilitiesSector = yf.Ticker('^SP500-55')
realEstateSector = yf.Ticker('^SP500-60')
print()

# check for stocks that have a SMA21 > SMA200