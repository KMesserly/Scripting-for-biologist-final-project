# **Python Vizualization Tutorial**
This tutorial will walk you through three diffrent vizualization techniques in python. All of the code is written in GitBash which is a BASH emulator within a windows system. You will need Python 3 installed I recommend doing this through Anaconda (https://www.anaconda.com/products/individual). After you have GitBash and Python 3 installed you have everything you need to strt the tutorial!

The first step in the data visualization process is cleaning and prepping the data. This step is different depending on the type of data format or the file you are visualizing. For our example, we willb be using data from the Pan-European Common Bird Monitoring Scheme. This data set tracks the population sizes of common bird species in Europe. Specificallly I have provided a file named "population.csv" which includes the bird species that the Pan-European Common Monitoring Scheme started recording population size for in 1980. The species in "population.csv" were initially sampled in 1990 and the recorded data looks at the index % change in population size since that initial sampling in 1990 until 2021.


# Scripts
1. **line_chart.py** - this script creates a line graph that shows the trends in the relative change in population of different European bird species over time. The final visualization is saved as a PNG image file.

2. **heat_map.py** -  This script visualizes the relative change in European bird population over time and across different species by using the seaborn package to create a heatmap from a pivot table. The final visualization is saved as a PNG image file.

3. **area_chart.py** - This script visualizes data using the seaborn and matplotlib.pyplot libraries to create an area chart that displays the relative change in population for each bird species over time. The final visualization is saved as a PNG image file. 


# External Packages
**pandas** - is a Python library for data manipulation and analysis. It provides data structures for efficiently storing and manipulating large datasets and tools for data cleaning, aggregation, and analysis.

**matplotlib.pyplot** - is a Python library for creating static, animated, and interactive visualizations in Python. It provides a range of functions for creating line plots, scatter plots, bar plots, histograms, 3D plots, and more.

**seaborn** - is a Python data visualization library based on Matplotlib. It provides a high-level interface for creating informative and attractive statistical graphics. Seaborn is particularly suited for working with complex datasets and for creating sophisticated statistical visualizations.

**preprocessing** - is a package in scikit-learn that provides a range of functions for preprocessing data prior to modeling. It includes functions for scaling data, transforming data, handling missing values, encoding categorical variables, and more. These functions are designed to ensure that data is in an appropriate format and that any issues or inconsistencies are resolved prior to modeling.

