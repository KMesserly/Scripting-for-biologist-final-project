import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

#Load the data into a pandas dataframe
population_long = pd.read_csv("population.csv")

#Long-form data
print(population_long.head())

#Create a pivot table
pivot_population = population_long.pivot_table(index='year', columns='species', values='change', aggfunc='mean')

#Create the heatmap using seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(pivot_population, cmap='coolwarm', annot=True, fmt='.1f', annot_kws={"fontsize": 10})
plt.xlabel('Species', fontsize=12)
plt.ylabel('Year', fontsize=12)
plt.title('Heatmap Showing the Relative Change in European Bird Population', fontsize=14)
plt.savefig("heat_map.png", dpi=300, bbox_inches='tight')
