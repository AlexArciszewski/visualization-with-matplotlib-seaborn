import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


df = pd.read_excel(
    r"C:\Dane\2_Python_Data\999_Zbiory danych\firma.xlsx",
    sheet_name ='Arkusz1',
    names= ['Data', 'Kosty', 'Przychody', 'Wynik finansowy', 'Wspolpraca','Liczba pracownikow' ]
    )
print(df.head(2))


df['Data'] = pd.to_datetime(df['Data'])

x = df['Data']
y = df['Wynik finansowy']
print(plt.plot(x, y, label='Wynik finansowy')) #dodajemy label
plt.title('wynik finansowy przedsiebiorstwa')
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
plt.savefig('test_001.jpg')
print(plt.plot(x,df['Przychody'],label='Przychody')) #dodajemy label
# plt.legend(['Wynik finansowy','Przychody'])
plt.legend()
plt.show()