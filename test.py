
import csv
import sys
import pandas as pd

level = []
data_df = pd.read_csv('stat.csv')
levels = data_df['niveau'].value_counts(normalize=True)
for f in levels:
    level.append(f)

print(level)