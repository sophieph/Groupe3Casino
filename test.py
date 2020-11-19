
import csv
import sys
import pandas as pd

level = []
data_df = pd.read_csv('stat.csv')

data_df[data_df['niveau'] == 1]['gain'].mean()
niveau_1 = data_df[data_df['niveau'] == 1]['gain'].mean()  
niveau_2 = data_df[data_df['niveau'] == 2]['gain'].mean()  
niveau_3 = data_df[data_df['niveau'] == 3]['gain'].mean()
winningArray = []
winningArray.append(niveau_1)
winningArray.append(niveau_2)
winningArray.append(niveau_3)
    
print(winningArray)