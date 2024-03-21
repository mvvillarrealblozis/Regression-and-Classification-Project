import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import classification_report, accuracy_score, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# Load the dataset
clothingData = pd.read_csv('dataset/Womens-Clothing-E-Commerce-Reviews.csv')
print(clothingData.head())

# Preprocess the dataset
clothingData = clothingData.drop(columns=['Unnamed: 0'])  # Remove the unnamed column
# Fill missing values for categorical columns with 'Unknown'
clothingData.fillna({'Division Name': 'Unknown', 'Department Name': 'Unknown', 'Class Name': 'Unknown'}, inplace=True)

# For machine learning, we're interested in Age, Rating, Department Name, Class Name, and Recommended IND
features = ['Age', 'Rating', 'Department Name', 'Class Name']
target_classification = 'Recommended IND'
target_regression = 'Positive Feedback Count'

# Prepare data for classification
X = pd.get_dummies(clothingData[features], drop_first=True)
y_classification = clothingData[target_classification]
y_regression = clothingData[target_regression]

# Splitting the dataset into training and testing sets for classification
X_train_class, X_test_class, y_train_class, y_test_class = train_test_split(X, y_classification, test_size=0.3, random_state=42)

# Define a preprocessing pipeline for scaling features
scaler = StandardScaler()

# Classification with Logistic Regression
logistic_regression_pipeline = Pipeline(steps=[('scaler', scaler), ('logistic', LogisticRegression(max_iter=1000))])
logistic_regression_pipeline.fit(X_train_class, y_train_class)
predictions_class = logistic_regression_pipeline.predict(X_test_class)
accuracy_class = accuracy_score(y_test_class, predictions_class)
classification_rep = classification_report(y_test_class, predictions_class)

print(f'Classification Accuracy: {accuracy_class}\n')
print(f'Classification Report:\n{classification_rep}')

# Regression with Linear Regression
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X, y_regression, test_size=0.3, random_state=42)

linear_regression_pipeline = Pipeline(steps=[('scaler', scaler), ('linear', LinearRegression())])
linear_regression_pipeline.fit(X_train_reg, y_train_reg)
predictions_reg = linear_regression_pipeline.predict(X_test_reg)
mse = mean_squared_error(y_test_reg, predictions_reg)
r2 = r2_score(y_test_reg, predictions_reg)

print(f'Regression MSE: {mse}')
print(f'Regression R^2: {r2}')
