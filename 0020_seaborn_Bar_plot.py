import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

sns.barplot(x='smoker', y='tip', data=df)
plt.show()

#zmiana kolorystyki:

sns.barplot(x='smoker', y='tip', data=df, palette={'Yes': 'tomato', 'No': 'skyblue'})
plt.show()


sns.barplot(x='smoker', y='tip', data=df, palette="Set2")
plt.show()


sns.barplot(x='smoker', y='tip', data=df, estimator=np.median, palette="Set2")
plt.show()


sns.barplot(x='smoker', y='tip', data=df, estimator=np.std, palette="Set1")
plt.show()

#Bar plots są wykorzystywane do zobrazowania rozkładu zmiennej kategorycznej. Aby stworzyć bar plot za pomocą seaborn wystarczy użyć funkcji sns.barplot() i dodać argumenty: x, y oraz data
#czarne kreski – są to tak zwane linie niepewności. Im dłuższa linia niepewności, tym bardziej zmienne potrafią być napiwki dla konkretnej grupy.