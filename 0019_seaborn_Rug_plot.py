
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#tam gdzie na wykresie występuję bardzo dużo kresek, tam też jest najwięcej obserwacji.
sns.rugplot(df['tip'])
plt.show()


#rugplot wykorzystuje się w połączeniu z jakimś innym wykresem, np. KDE plot:

sns.kdeplot(df['tip'])
sns.rugplot(df['tip'])
plt.show()