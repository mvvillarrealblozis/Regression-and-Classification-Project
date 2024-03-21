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

#print(missingValues, numericalSummary, uniqueDivisionNames, uniqueDepartmentNames, uniqueClassNames)


# Fill missing values for categorical columns with 'Unknown'
clothingData.fillna({'Division Name': 'Unknown', 'Department Name': 'Unknown', 'Class Name': 'Unknown'}, inplace=True)

# Check again to confirm that missing values are handled
missing_values_after = clothingData.isnull().sum()

# For classification, we're interested in Age, Rating, Department Name, Class Name, and Recommended IND
featuresClassification = ['Age', 'Rating', 'Department Name', 'Class Name']
targetClassification = 'Recommended IND'

# Convert categorical features to dummy variables
dfClassification = pd.get_dummies(clothingData[featuresClassification], drop_first=True)
dfClassification['Recommended IND'] = clothingData[targetClassification]

#print(missing_values_after, df_classification.head())


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Separate features and target variable for classification
X_classification = dfClassification.drop('Recommended IND', axis=1)
y_classification = dfClassification['Recommended IND']

# Splitting the dataset into training and testing sets
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X_classification, y_classification, test_size=0.3, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_class_scaled = scaler.fit_transform(X_train_class)
X_test_class_scaled = scaler.transform(X_test_class)

# Initialize and train logistic regression model
logisticRegression = LogisticRegression(max_iter=1000)
logisticRegression.fit(X_train_class_scaled, y_train_class)

# Predictions and evaluation
predictionsClass = logisticRegression.predict(X_test_class_scaled)
accuracy = accuracy_score(y_test_class, predictionsClass)
classification_rep = classification_report(y_test_class, predictionsClass)

print(accuracy, classification_rep)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


target_regression = 'Positive Feedback Count'

