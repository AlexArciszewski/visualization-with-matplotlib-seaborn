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

sns.displot(df['total_bill'],kde=True)
plt.show()

#kde=True, dzięki któremu widzimy jak kształtuje się teoretyczny rozkład danych linia ciągla.

#jako argument podając dane, których rozkład chcemy przedstawić i opcjonalny argument kde=True, 
# dzięki któremu widzimy jak kształtuje się teoretyczny rozkład danych.

#Na naszym wykresie występuję zauważalna asymetria prawostronna, co oznacza, że większość osób miało rachunek niższy, niż przeciętny rachunek.
#spłaszczenie rozkładu. Im wyższy „dzwon” tym wartości są bardziej skupione wokół średniej. Im bardziej spłaszczony dzwon, tym obserwacje są mniej skupione wokół średniej.
#Na podstawie powyższego histogramu możemy również odczytać, że najwięcej osób miało rachunek od 10 do 20 dolarów, oraz że najwyższy rachunek wynosił około 50 dolarów.
#sns.displot(df['total_bill'], kde=True, bins=10) bins=10 prostokątów zostanie wyświetlone.

#liczba prostokątow
sns.displot(df['total_bill'], kde=True, bins=40)
plt.show()