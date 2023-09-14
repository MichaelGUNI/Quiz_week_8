import matplotlib.pyplot as plt
import pandas as pd

years = []
co2 = []
temp = []

df = pd.read_csv(r"climate.csv")
pandaYear = df["Year"]
pandaCo2 = df["CO2"]
pandaTemp = df["Temperature"]

for i in range(len(pandaCo2)):
    years.append(pandaYear[i])
for i in range(len(pandaCo2)):
    co2.append(pandaCo2[i])
for i in range(len(pandaTemp)):
    temp.append(pandaTemp[i])

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_2.png") 

