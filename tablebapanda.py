
"""
# save thae data as it represented  
import pandas as pd

tables = pd.read_html('http://www.fipiran.com/Market/LupBourse',header=0)

print(tables[0])

tables[0].to_csv('pandatabburs.csv')

"""

# save thae data as decreasingly

import pandas as pd

tables = pd.read_html('http://www.fipiran.com/Fund/MFComparing/3',header=0)

data=tables[0]


#data.dtypes

#data.columns.values

"to remove M character and ,"
datam=data.replace('M','',regex=True)

datam=datam.replace(',','',regex=True)

#datam.dtypes

datam=datam[1:]
#this columns value is objective and I change it to int

datam[  'a']=datam[  'خالص ارزش دارایی صندوق(ریال)'].astype('int64')*1000000
datam[  'ارزش خالص هر واحد سرمایه گذاری (NAV)(ریال)'].astype('int64')


datam['تعداد واحدهای سرمایه گذاری']=datam[ 'a']/datam['ارزش خالص هر واحد سرمایه گذاری (NAV)(ریال)']


datas=datam.sort_values(by=['بازدهی ماه(%)'],ascending=False)


datas.to_csv('pandatabsandogh.csv')
