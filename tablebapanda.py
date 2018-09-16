
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


data.columns.values

datas=data.sort_values(by=['بازدهی ماه(%)'],ascending=False)


datas.to_csv('pandatabsandogh.csv')

