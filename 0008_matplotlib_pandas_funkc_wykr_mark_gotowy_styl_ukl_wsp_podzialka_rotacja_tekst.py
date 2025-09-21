import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df =  pd.read_excel(
    r"C:\Dane\2_Python_Data\999_Zbiory danych\firma.xlsx",
    sheet_name = 'Arkusz1',
    names = ['Data', 'Kosty', 'Przychody', 'Wynik finansowy', 'Wspolpraca','Liczba pracownikow' ]
    )
print(df.head(2))
df['Data'] = pd.to_datetime(df['Data'])
df['Data_str'] = df['Data'].apply(lambda x:x.strftime("%Y-%m"))
# print(df['Data_str'])
print(df.info())

#przypisanie danych

x = df['Data']
x2 = df['Data_str']
y = df['Wynik finansowy']
#wykresy i ich opis
#skrocony zapis zamiast poniższego
#plt.plot(x,y, marker='o', linestyle='--', color='b', label='Wynik finansowy')   #można użyć hex string za kolor kolor linestyle marker skracamy
#plt.plot(x,y, 'b--o', label='Wynik finansowy')

plt.style.use('ggplot')#gotowy styl
plt.plot(x2,y,marker='o',linestyle='--', color='b', linewidth=2,label='Wynik finansowy')
plt.plot(x2,df['Przychody'], marker='x', color='r', label='Przychody')
#markery->, _ o x + - X D - 

#podzialka na osi
plt.yticks([-400, -300, -200, -100, 0, 100, 200, 300, 400, 500, 600, 700, 800])
#plt.xticks(rotation=45)
#zmiana aby grancie podać
plt.xticks(['2014-01','2015-09'], rotation=45)
#opisy osi
plt.xlabel('Data')
plt.ylabel('Wynik finansowy')
#tytuł wykresu
plt.title('Wynik finansowy organizacji')
#tekst
plt.text('2014-01', 600, 'Ala ma kota')
plt.legend(loc=2)
plt.grid(True)
plt.show()