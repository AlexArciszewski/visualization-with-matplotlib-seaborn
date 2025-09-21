import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#Alternatywa dla strip plot jest swarm plot, który umieszcza kropki obok siebie, dzięki czemu czytelność wykresu jest większa (kropki na siebie nie nachodzą).
sns.swarmplot(x='smoker', y='tip', data=df)
plt.show()
#Opcja rozszerzona
sns.swarmplot(x='smoker', y='tip', data=df, hue='sex', palette='Set1')
plt.show()