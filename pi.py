# Apriori


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('pipostgre.csv', header = None)
#pipostgre is the csv of file of pipostgre which has modified to one row for each user

"""tedad= pd.read_csv('tedad.csv')

plt.plot(tedad[1],tedad[0])

plt.show()"""


#46 IS THE NUMBER OF OBSERVATION- THE NUMBER OF ROWS
#4 IS THE NUMBER OF MOST CATEGORIES WE WANT TO CONSIDER(NUMBER OF COULUMN)
transactions = []
for i in range(0, 46):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 4)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)

for i in results:
    print(i[0])
    print(i[2])
    print('\n')
