from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading the file and parsing the data to readable arrays
df = pd.read_excel(r"C:\Users\16476\OneDrive\Desktop\Kepler\ChallengeSampleData.xlsx")
x = list(df['Budget Codes'])
y = list(df['Line Cost'])
labels = list(df['LPP Currency'])
data = pd.DataFrame({"Budget Codes": x, "Line Cost": y, "Category": labels})

#plotting the data and creating the legend
groups = data.groupby("Category")
for name, group in groups:
    plt.plot(group["Budget Codes"], group["Line Cost"], marker="o", linestyle="", label=name)
plt.legend()

#creating the axis labels and title
ax = plt.gca()
ax.set_xticklabels(ax.get_xticks())
ax.set_yscale('log') #setting scale to logarithmic so all data fits and is more easily readable
ax.set_xlabel("Budget Codes")
ax.set_ylabel("Line Cost")
plt.title("Budget Codes v Line Cost")
plt.show() #printing the graph