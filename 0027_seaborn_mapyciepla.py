import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#Mapa ciepła
#Mapa ciepła w analizie danych jest używana do przedstawienia zależności między zmiennymi pokazując siłę zależności za pomocą kolorów.

# Zakładając, że masz już DataFrame df
df['smoker'] = df['smoker'].map({'No': 0, 'Yes': 1})

# Wybieramy tylko kolumny numeryczne
df_numeric = df.select_dtypes(include=['float64', 'int64'])

# Obliczamy korelację tylko dla danych numerycznych
df_map = df_numeric.corr()

# Wyświetlamy wynik
print(df_map.head())
#             total_bill       tip      size
# total_bill    1.000000  0.675734  0.598315
# tip           0.675734  1.000000  0.489299
# size          0.598315  0.489299  1.000000

sns.heatmap(df_map)
plt.show()

#annot czyli liczby pokazujące zaleznosć
sns.heatmap(df_map, annot=True)
plt.show()

#annot czyli liczby pokazujące zaleznosć +cmap kolorystyka
sns.heatmap(df_map, annot=True, cmap='inferno')
plt.show()
