import eikon as ek

data = ek.get_timeseries('AAPL.0', fields='*',
                         start_date='2022-01-01',
                         end_date='2022-01-20')

print(data.tail())
