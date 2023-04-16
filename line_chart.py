import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing


# load the data into a pandas dataframe
population_long = pd.read_csv("population.csv")

#Long-form data
print(population_long.head())

# Set a custom color palette
colors = ["#1f77b4", "#ff7f0e"]
sns.set_palette(sns.color_palette(colors))

# Plot the trends for each species
p = sns.relplot(data=population_long, x="year", y="change", hue="species", kind="line", height=5, aspect=2)
p.set(xlabel="Year", ylabel="Relative Change in European Bird Population", title="Relative Population Change by European Bird Species")
p.tight_layout()
p.savefig("line_chart.png", dpi=300)

# Move the legend to the lower left of the plot
p._legend.set_bbox_to_anchor((0, 0.5))
