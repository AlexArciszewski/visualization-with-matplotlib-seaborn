import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#count plot rozkłady liczebności zmiennych kategorycznych.

sns.countplot(x='sex', data=df, palette='Set2')
plt.show()

sns.countplot(x='sex', data=df, hue='smoker', width=0.5)
plt.show()

ax = sns.countplot(x='sex', data=df)
ax.set_title("Rozkład płci")
ax.set_xlabel("Płeć")
ax.set_ylabel("Liczba osób")
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.show()