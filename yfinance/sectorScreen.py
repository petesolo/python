import pandas as pd
import yfinance as yf

stocksCSV = 'https://datahub.io/core/s-and-p-500-companies/r/constituents.csv'
spxStocks = pd.read_csv(stocksCSV)
primeList = pd.DataFrame(columns=['Stock','Current Price','YTD High','YTD Low','Current Volume','Average Volume','Six Month Return','Twelve Month Return'])

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

