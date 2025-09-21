import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Dane\2_Python_Data\999_Zbiory danych\zawodnicy.xlsx',sheet_name='Arkusz1', names= ["Imie", "Liczba goli", "Pozycja","Liczba meczy", "Pierwszy sklad","Wartosc zawodnika","Zdjecie zawodnika"])
print(df.head(2))
df.drop('Zdjecie zawodnika',axis=1, inplace=True)
df.drop(0,inplace=True)
df.info()

print(df)

goals_first = df[df['Pierwszy sklad'] == 'Tak']['Liczba goli'].sum()
goals_reserve = df[df['Pierwszy sklad'] == 'Nie']['Liczba goli'].sum()

plt.pie(
    [goals_first, goals_reserve],
    labels=['Pierwszy sklad', 'Rezerwowi'],
    autopct='%1.1f%%'  #sprawia, że na wykresie będą wyświetlone wartości procentowe z dokładnością do jednego miejsca po przecinku.
)
plt.show()