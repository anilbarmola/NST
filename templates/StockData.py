import yfinance as yf

nifty_data = yf.download('^NSEI', start='2023-08-01', end='2023-09-02', interval='30m')

nifty_data['Price_Difference_High'] = nifty_data['High'] - nifty_data['Open']
nifty_data['Price_Difference_Low'] = nifty_data['Low'] - nifty_data['Open']

count_high_greater_by_10_and_low_not_less_by_5 = ((nifty_data['Price_Difference_High'] >= 10) & (nifty_data['Price_Difference_Low'] >= -5)).sum()

print("Number of times High Price is greater than Open Price by 10 and Low Price is not 5 less than Open Price:", count_high_greater_by_10_and_low_not_less_by_5)
