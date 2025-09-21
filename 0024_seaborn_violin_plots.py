import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#W środku każdej figury znajduje się wykres pudełkowy. Wykres ten jest otoczony podwójnym wykresem kde
sns.violinplot(x='smoker', y='tip', data=df,palette={'Yes': 'skyblue', 'No': 'red'})
plt.show()


sns.violinplot(x='smoker', y='tip', data=df,hue='sex', palette={'Yes': 'skyblue', 'No': 'red','Male':'darkblue', 'Female':'pink'})
plt.show()

sns.violinplot(x='smoker', y='tip', data=df,hue='sex', palette={'Yes': 'skyblue', 'No': 'red','Male':'darkblue', 'Female':'pink'}, split=True)
plt.show()