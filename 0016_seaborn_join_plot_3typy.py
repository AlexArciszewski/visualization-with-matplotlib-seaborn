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

sns.jointplot(x = 'total_bill', y = 'tip', data=df)
plt.show()

# Wykres składa się z trzech oddzielnych wykresów. Na górze znajduje się distribution plot zmiennej x total_bill, po prawej stronie znajduje się distribution plot zmiennej y tip a pośrodku znajduje się wykres rozrzutu badanych zmiennych.


# Możemy teraz dodać argument kind i przypisać mu wartość reg aby do naszego wykresu rozrzutu dodać linię regresji i jednocześnie do wykresów rozkładu linie kde:

sns.jointplot(x = 'total_bill', y = 'tip', data=df, kind='reg')
plt.show()



# Wykres ten prezentuje histogramy obu zmiennych oraz histogram zbiorczy (im ciemniejszy kolor tym suma wartości z poszczególnych #histogramów jest większa).

sns.jointplot(x = 'total_bill', y = 'tip', data=df, kind='hist')
plt.show()