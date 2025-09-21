import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#Striplot:
#Wykres ten przedstawia uporządkowane wartości zmiennej względem jednej osi układu współrzędnych.

sns.stripplot(x='smoker', y='tip', data=df, jitter=True)
plt.show()
#różne kolory w zaleznosci od zmiennej sex
sns.stripplot(x='smoker', y='tip', data=df, jitter=True, hue='sex')
plt.show()
#palette
sns.stripplot(x='smoker', y='tip', data=df, jitter=True, hue='sex', palette='Set1')
plt.show()
#dodge rozdział wykresu na 4 części

sns.stripplot(x='smoker', y='tip', data=df, jitter=True, hue='sex', palette='Set1', dodge=True)
plt.show()