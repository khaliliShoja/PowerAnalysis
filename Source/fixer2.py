import pandas as pd
from glob import glob


Files = glob('..\Data\Power\*.csv')
Tall = pd.DataFrame()
for f in Files:
    T = pd.read_csv(f)
    T['Date'] = T['Date'].apply(lambda x: x.replace('*', '')) # there was an * in one file 10022009to11022009.csv
    T['Date'] = pd.to_datetime(T['Date'].apply(lambda x: x[:-2]+'%0.2d' % (int(x[-2:])-1)), format='%m/%d/%Y %H')
    for c in ['Day-Ahead Forecasted AIL', 'Actual AIL']:
        T[c] = T[c].apply(lambda x: float(x.replace(',', '')))
    T = T.set_index('Date')
    Tall = pd.concat([Tall, T])

Tall = Tall.sort_index()
Tall.to_csv('..\Data\Power\\fixed\\df_all.csv')
