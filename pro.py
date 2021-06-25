import csv
import pandas as pd
import statistics as st

data = pd.read_csv('data.csv')

list = data['Weight(Pounds)'].tolist()

mean = st.mean(list)
median = st.median(list)
mode = st.mode(list)

print('mean = ', mean)
print('mode = ', mode)
print('median = ', median)