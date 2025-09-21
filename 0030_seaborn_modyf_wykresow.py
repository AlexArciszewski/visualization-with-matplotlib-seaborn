import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())


#połączenie styli:white oraz darkgrid.
sns.set_style('white')
sns.jointplot(x=df['total_bill'], y=df['tip'], data=df, kind='reg')
plt.show()


#napisy sns.set_context() Paper – styl napisów, który powinniśmy używać na papierze


sns.set_style('darkgrid')
sns.set_context('paper', font_scale=2)  #zapis jak na papierze
sns.jointplot(x=df['total_bill'], y=df['tip'], data=df, kind='reg')
plt.show()


#talk styl dopasowany do prezentacji
sns.set_style('darkgrid')
sns.set_context('talk', font_scale=2)  #zapis jak na prezentacji
sns.jointplot(x=df['total_bill'], y=df['tip'], data=df, kind='reg')
plt.show()


#poster styl dopasowany do plakatu
sns.set_style('darkgrid')
sns.set_context('poster', font_scale=2)  #zapis jak na plakacie
sns.jointplot(x=df['total_bill'], y=df['tip'], data=df, kind='reg')
plt.show()


#usunięcie osi układu współprzędnych despine zwiekszamy wykres

sns.set_style('darkgrid')
sns.set_context('paper', font_scale=2)  #zapis jak na plakacie
#sns.jointplot(x=df['total_bill'], y=df['tip'], data=df, kind='reg')
sns.jointplot(x=df['total_bill'], y=df['tip'], data=df, kind='reg', height=10) #zwiększamy wykres
sns.despine(left=True, bottom=True) #usuneicie ukl wsp
plt.show()

