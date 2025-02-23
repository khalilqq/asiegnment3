import pandas as pd

df = pd.read_csv('iris_dataset.csv')

print("Dataset Overview:")
print(df.head())

correlation_matrix = df.corr()
print("\nCorrelation Matrix:")
print(correlation_matrix)

stats_summary = df.groupby('species').agg(['mean', 'median', 'std'])

stats_summary.to_csv('iris_statistics.csv')

species_correlation = df.groupby('species').corr()
print("\nSpecies-Wise Correlation Matrix:")
print(species_correlation)

print("\nAnalysis complete. Statistical summary saved as 'iris_statistics.csv'.")
