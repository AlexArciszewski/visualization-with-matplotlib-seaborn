import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


df =  pd.read_excel(
    r"C:\Dane\2_Python_Data\999_Zbiory danych\firma.xlsx",
    sheet_name = 'Arkusz1',
    names = ['Data', 'Kosty', 'Przychody', 'Wynik finansowy', 'Wspolpraca','Liczba pracownikow' ]
    )
print(df.head(2))
df['Data'] = pd.to_datetime(df['Data'])


x = df['Data']
y = df['Wynik finansowy']
print(plt.plot(x,y,'b--o', color='red',label='Wynik finansowy'))
plt.title('Wynik finansowy przedsiębiorstwa')
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
plt.savefig('test_002.jpg')
print(plt.plot(x, df['Przychody'],'--o',label='Przychody',color='#444444'))
plt.legend()
plt.grid(True)
plt.show()




