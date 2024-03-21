import pandas as pd

clothingData = pd.read_csv('dataset/Womens-Clothing-E-Commerce-Reviews.csv')

print(clothingData.head())

# Remove the unnamed column
clothingData = clothingData.drop(columns=['Unnamed: 0'])

# Check for missing values
missingValues = clothingData.isnull().sum()

# Summary statistics for numerical columns
numericalSummary = clothingData.describe()

# Check unique values for categorical columns to understand their distribution
uniqueDivisionNames = clothingData['Division Name'].unique()
uniqueDepartmentNames = clothingData['Department Name'].unique()
uniqueClassNames = clothingData['Class Name'].unique()

print(missingValues, numericalSummary, uniqueDivisionNames, uniqueDepartmentNames, uniqueClassNames)
