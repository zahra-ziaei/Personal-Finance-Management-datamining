
import pandas as pd

tables = pd.read_html('http://www.fipiran.com/Fund/MFComparing/1',header=0)

print(tables[0])

tables[0].to_csv('pandatab.csv')
