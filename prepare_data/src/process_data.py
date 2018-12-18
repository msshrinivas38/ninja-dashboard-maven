import pandas as pd
import numpy as np
import datetime as dt
import calendar as cal


m_df = pd.read_csv("./prepare_data/data/raw/all_sentimet_fx.csv")

m_df['Date1'] = pd.to_datetime(m_df['Date1'])

m_df.sort_values(by=['Date1'],ascending=True)


friday_df = pd.DataFrame(m_df[m_df.Date1.dt.weekday_name == "Friday"])

friday_df["No_of_shares"]=10

friday_df["Bought"] = friday_df["No_of_shares"]*friday_df['Close']

agg_df = friday_df.groupby('Stock').agg({'Bought': 'sum',   
                                     'No_of_shares':'sum'
                                             })


agg_df['High'] = m_df.groupby('Stock').agg({'High':'max'})

agg_df['Low'] = m_df.groupby('Stock').agg({'Low':'min'})

agg_df['Bought']=round(agg_df['Bought']/agg_df['No_of_shares'],2)

m_df.sort_values

agg_df['CurrentPrice']=m_df.groupby('Stock').agg({'Close':'last'})

agg_df['Gain'] = round((agg_df['CurrentPrice']*agg_df['No_of_shares']-agg_df['Bought']*agg_df['No_of_shares'])/(agg_df['Bought']*agg_df['No_of_shares'])*100,2)

agg_df.to_csv("./prepare_data/data/stock_analysis_V1.csv")
