import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # Upewnij się, że to jest zaimportowane

# Sprawdzamy dostępne zbiory danych Seaborn
print(sns.get_dataset_names())

# Wczytujemy zbiór danych "tips"
df = sns.load_dataset('tips')
print(df.head())

#Box plot obrazowanie zróżnicowania rozkładu, asymetrii rozkładu oraz wykrycie wartości odstających
sns.boxplot(x='sex', y='tip', data=df,palette={'Male': 'skyblue', 'Female': 'lightpink'})
plt.show()

# Zróżnicowanie wewnętrznych 50% populacji charakteryzuje środkowe pudełko (niebieskie dla mężczyzn i róz dla kobiet)
# Im szersze pudełko, tym większe zróżnicowanie wewnętrznych 50% populacji. Przykładowo na powyższym wykresie większym zróżnicowaniem wewnętrznych 50% populacji charakteryzują się mężczyźni.
# Za to odległość między górnym „wąsem” a dolnym stanowi zróżnicowanie całego rozkładu. Jak widzimy dolny wąs jest taki sam dla kobiet jak i mężczyzn, ale górny wąs jest zdecydowanie wyżej dla mężczyzn. Czyli zróżnicowanie całego rozkładu jest również wyższe u mężczyzn.
# Zróżnicowanie 50% wewnętrznych obserwacji to zróżnicowanie 25% obserwacji pod medianą oraz 25% obserwacji nad medianą. To zróżnicowanie nie bierze pod uwagę obserwacji z bardzo małą lub wysoką wartością, więc jest odporne na tzw. wartości odstające.
# Zróżnicowanie całej populacji bierze pod uwagę wszystkie obserwacje. Przez to właśnie bardzo często jest ono zaburzone przez występowanie wartości odstających, czyli obserwacji posiadających bardzo małą lub bardzo wysoką wartość.
# Asymetria lewostronna występuję, gdy odległość między pudełkiem, a dolnym wąsem jest zdecydowanie większa, niż odległość między pudełkiem a górnym wąsem.
# Asymetria prawostronna występuję, gdy odległość między pudełkiem, a dolnym wąsem jest zdecydowanie mniejsza, niż odległość między pudełkiem a górnym wąsem.
# Symetria występuję, gdy obie te odległości są sobie równe.
# Z powyższego wykresu można wywnioskować, że rozkłady napiwków zarówno wśród kobiet jak i mężczyzn są prawostronnie asymetryczne.
# Wszystkie kropki znajdujące się nad górnym wąsem i pod dolnym wąsem są to tzw. wartości odstające, czyli wartości które są niespotykanie wysokie lub niskie. Przykładem takiej wartości jest na przykład napiwek o wysokości 10 dolarów.