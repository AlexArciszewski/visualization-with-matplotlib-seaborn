
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd



df =pd.read_excel('C:/Dane/2_Python powt_cale/001_python_all/001_2024_Python_exam_repetition/Zbiory danych/firma.xlsx')


print(df.head())
df['Data'] = pd.to_datetime(df['Data'])
print(df.info())
#przypisanie dnaych
x=df['Data']
y=df['Wynik finansowy']
#wykresy i ich opis
#skrocony zapis zamiast poniższego
#plt.plot(x,y, marker='o', linestyle='--', color='b', label='Wynik finansowy')   #można użyć hex string za kolor kolor linestyle marker skracamy
#plt.plot(x,y, 'b--o', label='Wynik finansowy')

#Zmiana poziałki na osi z użyciem lambda:
df['Data_str'] =  df['Data'].apply(lambda x:x.strftime("%Y-%m"))
print(df['Data_str'].head())
x2=df['Data_str']

plt.style.use('ggplot') #gotowy styl

plt.plot(x2,y, marker='o', linestyle='--', color='b', linewidth=2, label='Wynik finansowy')  
plt.plot(x2, df['Przychody'],marker='x', color='r', label='Przychody')
#markery->, _ o x + - X D - 

#podziaka na osi
plt.yticks([-400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800])
#przedział danych nie wypisane wszystkie jak leci
plt.xticks(rotation=45)
#opisy osi
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
#tytuł wykresu
plt.title('Wynik finansowy organizacji')
#legenda
plt.legend(loc=2)
plt.grid(True)
plt.show()