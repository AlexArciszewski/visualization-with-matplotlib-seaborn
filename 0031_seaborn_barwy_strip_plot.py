import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#strip plot
sns.set_style('dark')
sns.set_context('talk')
sns.stripplot(x='smoker', y='tip', data=df, hue='sex')
plt.show()


#Inna kolorystyka
sns.set_style('dark')
sns.set_context('talk')
sns.stripplot(x='smoker', y='tip', data=df, hue='sex', palette='inferno')
plt.show()


#Inna kolorystyka
sns.set_style('dark')
sns.set_context('talk')
sns.stripplot(x='smoker', y='tip', data=df, hue='sex', palette='coolwarm')
plt.show()



#Inna kolorystyka
sns.set_style('dark')
sns.set_context('talk')
sns.stripplot(x='smoker', y='tip', data=df, hue='sex', palette='coolwarm')
plt.legend(loc=2)   #Legenda 1 góra praw 2góra lewo 3 dół lewo 4 dół prawy
plt.show()