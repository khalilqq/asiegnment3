Iris Dataset Analysis with Pandas
Purpose
This project is trying to perform heterogeneous data analysis using Python and the Pandas module. The dataset used is the Fisher’s Iris dataset, which contains physical measurements of three iris species. The analysis includes merging datasets, computing statistical measures, and drawing conclusions about species similarity.
Features
* Data Loading & Merging: Imports the dataset and structures it into a Pandas DataFrame.
* Statistical Computation: Calculates the correlation, mean, median, and standard deviation for each species.
* Species Comparison: Determines which species are most and least similar based on correlation analysis.
* Export Results: Saves the statistical summary to a CSV file.
Implementation
The script follows these steps:
1. Loads the dataset into a Pandas DataFrame.
2. Displays an overview of the dataset.
3. Computes the correlation matrix to analyze relationships between features.
4. Calculates mean, median, and standard deviation for each species.
5. Identifies the most and least similar species based on correlation values.
6. Saves the statistical summary as a CSV file.
Requirements
* Python 3.8+
* Pandas
* CSV file of the Iris Dataset (to be placed in the same directory as the script)
Usage
Run the script using:
python iris_analysis.py
Output
* Printed correlation matrix and statistical summaries in the console.
* iris_statistics.csv file containing computed statistical values.
Limitations
* Assumes that the dataset is correctly formatted and contains no missing values.
* The analysis is purely statistical and does not include machine learning-based classification.