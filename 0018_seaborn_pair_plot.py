import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %matplotlib inline


print(sns.load_dataset('tips'))

#      total_bill   tip     sex smoker   day    time  size
# 0         16.99  1.01  Female     No   Sun  Dinner     2
# 1         10.34  1.66    Male     No   Sun  Dinner     3
# 2         21.01  3.50    Male     No   Sun  Dinner     3
# 3         23.68  3.31    Male     No   Sun  Dinner     2
# 4         24.59  3.61  Female     No   Sun  Dinner     4
# ..          ...   ...     ...    ...   ...     ...   ...
# 239       29.03  5.92    Male     No   Sat  Dinner     3
# 240       27.18  2.00  Female    Yes   Sat  Dinner     2
# 241       22.67  2.00    Male    Yes   Sat  Dinner     2
# 242       17.82  1.75    Male     No   Sat  Dinner     2
# 243       18.78  3.00  Female     No  Thur  Dinner     2
df = sns.load_dataset('tips')



sns.pairplot(df)
plt.show()

# Jak widzimy zostały wyróżnione trzy zmienne: total_bill, tip oraz size. Wszystkie te zmienne są ilościowe. Na głównej przekątnej znajdują się histogramy, ponieważ na głównej przekątnej znajdują się zależności między tymi samymi zmiennymi.
# Poza przekątną znajdują się wykresy rozrzutu, dzięki którym możemy odczytać jakie zależności zachodzą między zmiennymi. Na przykład między wysokością napiwku a całkowitą kwotą za posiłek występuję dodatnia, dość silna zależność.
# Możemy urozmaicić te wykresy za pomocą argumentu hue, który definiuje w podziale na jaką zmienną kategoryczną mają zostać wykonane te wykresy. Na przykład możemy sprawdzić, jak te wyżej przedstawione zależności kształtują się w podziale na płeć kelnera:


sns.pairplot(df, hue='sex')
plt.show()
# Widzimy teraz, że za każdym razem na układzie współrzędnych przedstawione są dwa wykresy, jeden dla mężczyzn a drugi dla kobiet.





