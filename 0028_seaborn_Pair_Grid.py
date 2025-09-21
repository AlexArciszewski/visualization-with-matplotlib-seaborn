import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#Pair grid wiele wykresów.
#płutno
sns.PairGrid(df,hue='sex')
plt.show()
#za pomoca map robimy załadowanei wykresów 

#przypisanie wykresu do zmiennej grid wykresy rozrzutu
grid = sns.PairGrid(df,hue='sex')
grid.map(plt.scatter)
plt.show()



#przypisanie wykresu do zmiennej grid
grid = sns.PairGrid(df,hue='sex')
grid.map(plt.scatter)
grid.map_diag(plt.hist) #histogramy na gównej przekątnej
plt.show()





#przypisanie wykresu do zmiennej grid
grid = sns.PairGrid(df,hue='sex')

grid.map_diag(plt.hist) #histogramy na gównej przekątnej
grid.map_upper(plt.scatter) #nad diagnoal rozrzut
grid.map_lower(sns.kdeplot,n_levels=3) #wykresy kdeplot pod diagnonal
plt.show()
