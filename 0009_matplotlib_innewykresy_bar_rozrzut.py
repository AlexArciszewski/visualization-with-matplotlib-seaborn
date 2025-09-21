import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv(r"C:\Dane\2_Python_Data\999_Zbiory danych\data_csv.csv")
print(df.head(2))

df.info()
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1768 entries, 0 to 1767
# Data columns (total 10 columns):
#  #   Column                Non-Null Count  Dtype  
# ---  ------                --------------  -----  
#  0   Date                  1768 non-null   object 
#  1   SP500                 1768 non-null   float64
#  2   Dividend              1767 non-null   float64
#  3   Earnings              1764 non-null   float64
#  4   Consumer Price Index  1768 non-null   float64
#  5   Long Interest Rate    1768 non-null   float64
#  6   Real Price            1768 non-null   float64
#  7   Real Dividend         1767 non-null   float64
#  8   Real Earnings         1764 non-null   float64
#  9   PE10                  1648 non-null   float64
# dtypes: float64(9), object(1)
# memory usage: 138.3+ KB

#Zmieniamy object do Data
df['Date'] = pd.to_datetime(df['Date'])

x = df['Date']
y = df['SP500']
print(plt.plot(x,y))
plt.show()


print(plt.bar(x,y,width=33))
plt.show()


df2 = pd.read_excel(r'C:\Dane\2_Python_Data\999_Zbiory danych\dane.xlsx',sheet_name='Zarzad', names= ["Imie", "Wiek", "Wzrost",	"Miasto", "Waga"])
print(df2.head(2))

print(plt.bar(df2['Miasto'].unique(), df2['Miasto'].value_counts()))
plt.show()