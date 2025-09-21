import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())



#Facet grid jest to kolejne narzędzie, które pozwoli nam na przedstawienie kilku wykresów obok siebie.
#pusty uklad współ
mapa =  sns.FacetGrid(df, col='time', row='smoker')
plt.show()

#histogramy
mapa =  sns.FacetGrid(df, col='time', row='smoker')
mapa.map(plt.hist, 'total_bill')
plt.show()

mapa =  sns.FacetGrid(df, col='time', row='smoker')
mapa.map(plt.hist, 'tip')
plt.show()

