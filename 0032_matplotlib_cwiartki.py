import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df1 = sns.load_dataset('exercise')
df2 = sns.load_dataset('mpg')
df3 = sns.load_dataset('tips')

# Tworzenie wykresów
figure, axes = plt.subplots(2, 2, figsize=(10, 10))

axes[0,0].pie(df2['origin'].value_counts(), labels=df2['origin'].unique(), autopct='%1.2f%%',
              colors=['pink', 'blue', 'green'],
              textprops={'fontsize':14})

axes[1,1].scatter(x=df2['weight'], y=df2['horsepower'])
axes[1,0].bar(df1['diet'].unique(), df1['diet'].value_counts())
axes[0,1].barh(df1['kind'].unique(), df1['kind'].value_counts())
plt.show()



'''1. Tworzenie siatki wykresów:

figure, axes = plt.subplots(2,2, figsize=(10,10))

plt.subplots(2,2, figsize=(10,10)) – Tworzy siatkę wykresów w układzie 2x2 (2 wiersze, 2 kolumny) o rozmiarze 10x10 cali.
figure – To cały obiekt wykresu (możemy go modyfikować, np. dodać tytuł).
axes – To tablica, zawierająca poszczególne osie wykresów (axes[0,0], axes[0,1], axes[1,0], axes[1,1]).
2. Wykres kołowy (Pie Chart) w lewym górnym rogu:

axes[0,0].pie(df2['origin'].value_counts(), 
              labels=df2['origin'].unique(), 
              autopct='%1.2f%%',
              colors=['pink','blue','green'],
              textprops={'fontsize':14})

axes[0,0].pie(...) – Rysuje wykres kołowy.
df2['origin'].value_counts() – Liczy wystąpienia każdej wartości w kolumnie "origin" i przekazuje jako wartości do wykresu.
labels=df2['origin'].unique() – Tworzy etykiety dla segmentów wykresu (np. kontynenty pochodzenia samochodów).
autopct='%1.2f%%' – Pokazuje wartości w procentach z dokładnością do dwóch miejsc po przecinku.
colors=['pink','blue','green'] – Ustawia kolory segmentów wykresu.
textprops={'fontsize':14} – Powiększa czcionkę opisów do 14.
3. Wykres punktowy (Scatter Plot) w prawym dolnym rogu:

axes[1,1].scatter(x = df2['weight'], y = df2['horsepower'])

axes[1,1].scatter(...) – Rysuje wykres punktowy (scatter plot).
x = df2['weight'] – Oś X to waga samochodu.
y = df2['horsepower'] – Oś Y to moc silnika.

Ten wykres pokazuje, jak moc silnika zależy od wagi samochodu.
4. Wykres słupkowy pionowy (Bar Chart) w lewym dolnym rogu:

axes[1,0].bar(df1['diet'].unique(), df1['diet'].value_counts())

axes[1,0].bar(...) – Tworzy wykres słupkowy pionowy.
df1['diet'].unique() – Pobiera unikalne wartości diety np. ['wegetariańska', 'mięsna', 'wegańska'].
df1['diet'].value_counts() – Liczy, ile razy każda dieta występuje w danych.

 Wykres pokazuje popularność różnych diet.
5. Wykres słupkowy poziomy (Horizontal Bar Chart) w prawym górnym rogu:

axes[0,1].barh(df1['kind'].unique(), df1['kind'].value_counts())

axes[0,1].barh(...) – Tworzy wykres słupkowy poziomy.
df1['kind'].unique() – Pobiera unikalne wartości rodzaju zwierząt (np. ['ssak', 'gad', 'ptak']).
df1['kind'].value_counts() – Liczy, ile razy każdy rodzaj zwierzęcia występuje w danych.'''



















