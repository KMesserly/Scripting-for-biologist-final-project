
#Use the `import ... as ...` command to shorten each command
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
data = pd.read_csv('hsp_gene_expression.csv')

# Calculate the mean and standard deviation for each gene
gene_means = data.mean()
gene_stds = data.std()

# Create a heatmap of the gene expression values
sns.heatmap(data, cmap='coolwarm')

# Identify the genes with the highest expression values
top_genes = gene_means.nlargest(10)

# Plot a bar chart of the top 10 genes by expression value
plt.figure()
top_genes.plot(kind='bar')

# Perform a principal component analysis to identify patterns in the data
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(data)
transformed_data = pca.transform(data)
plt.figure()
plt.scatter(transformed_data[:, 0], transformed_data[:, 1])
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')

# Perform a t-test to compare the expression levels between two groups
group1 = data[data['group'] == 1]
group2 = data[data['group'] == 0]
t_vals, p_vals = [], []
for gene in data.columns:
    t_stat, p_val = ttest_ind(group1[gene], group2[gene])
    t_vals.append(t_stat)
    p_vals.append(p_val)
results = pd.DataFrame({'gene': data.columns, 't_value': t_vals, 'p_value': p_vals})
significant_genes = results[results['p_value'] < 0.05]['gene']
