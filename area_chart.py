import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

#Load the data into a pandas dataframe
population_long = pd.read_csv("population.csv")

#Long-form data
print(population_long.head())

#Create a grid: initialize it
g = sns.FacetGrid(population_long, col='species', hue='species', col_wrap=4)

#Add the line over the area with the plot function
g = g.map(plt.plot, 'year', 'change')

#Fill the area with fill_between
g = g.map(plt.fill_between, 'year', 'change', alpha=0.2).set_titles("{col_name} species")

#Control the title of each facet
g = g.set_titles("{col_name}")

#Add a title for the whole plot
g.fig.suptitle('Relative Change in European Bird Populations Since 1990', fontsize=16)

#Adjust the spacing between subplots
plt.subplots_adjust(top=0.9, hspace=0.5)

#Save the figure
g.savefig("Area_chart.png")
