import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline dla jb aby nie otwierał sie wykres w osobnym oknie

df = pd.read_excel(
    r"C:\Dane\2_Python_Data\999_Zbiory danych\firma.xlsx",
    sheet_name ='Arkusz1',
    names= ['Data', 'Kosty', 'Przychody', 'Wynik finansowy', 'Wspolpraca','Liczba pracownikow' ]
    )
print(df.head(2))


df['Data'] = pd.to_datetime(df['Data'])

print(df.info())

# angeIndex: 24 entries, 0 to 23
# Data columns (total 6 columns):
#  #   Column              Non-Null Count  Dtype         
# ---  ------              --------------  -----         
#  0   Data                24 non-null     datetime64[ns]
#  1   Kosty               24 non-null     int64         
#  2   Przychody           24 non-null     int64         
#  3   Wynik finansowy     24 non-null     int64         
#  4   Wspolpraca          24 non-null     object        
#  5   Liczba pracownikow  24 non-null     int64         
# dtypes: datetime64[ns](1), int64(4), object(1)
# memory usage: 1.3+ KB

print(df.plot(x="Data",y="Wynik finansowy"))
plt.title("Wynik finansowy w czasie")
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
plt.show()