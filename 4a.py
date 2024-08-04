

# Import necessary libraries
import pandas as pd

# Load a sample dataset (e.g., tips dataset from seaborn)
tips = pd.read_csv("(link unavailable)")

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(tips.head())

# Display the last few rows of the dataset
print("\nLast few rows of the dataset:")
print(tips.tail())

# Display information about the dataset (e.g., number of rows, data types)
print("\nDataset information:")
print(tips.info())

# Display summary statistics for the dataset
print("\nSummary statistics:")
print(tips.describe())

# Filter rows where the total bill is greater than $50
print("\nRows where total bill is greater than $50:")
print(tips[tips['total_bill'] > 50])

# Group the dataset by day and calculate the average tip
print("\nAverage tip by day:")
print(tips.groupby('day')['tip'].mean())

# Sort the dataset by total bill in descending order
print("\nDataset sorted by total bill in descending order:")
print(tips.sort_values('total_bill', ascending=False))

# Handle missing values (e.g., drop rows with missing values)
print("\nDataset after dropping rows with missing values:")
print(tips.dropna())


This program demonstrates the following basic operations using Pandas:

1. Loading a dataset from a CSV file
2. Displaying the first and last few rows of the dataset
3. Displaying information about the dataset (e.g., number of rows, data types)
4. Displaying summary statistics for the dataset
5. Filtering rows based on a condition
6. Grouping the dataset by a column and calculating a summary statistic
7. Sorting the dataset by a column in descending order
8. Handling missing values by dropping rows with missing values
