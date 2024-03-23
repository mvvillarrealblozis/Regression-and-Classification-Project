# BUS316-Final-Project Report

## Central Research Question
The core focus of this project was to analyze a Women’s Clothing E-Commerce dataset to understand the relationship between product reviews and customer recommendations,in addition to exploring factors influencing the positive feedback count. Here were the two questions that I focused on answering:

1. **Is there a connection between a customer's age, the product rating, and specific product categories (Department Name and Class Name) with whether a product is recommended (Recommended IND)?**
2. **Do these same variables have a connection with the positive feedback count received on a review?**

By answering these questions, I was able to gain a deeper understanding of customer behavior and satisfaction factors, which is critical in enhancing product recommendations and marketing strategies.

## Solution Approach
To address the questions, I performed two analytical approaches: **Classification and Regression**.

**Data Preprocessing**: The dataset is made of 23,486 rows and 10 feature variables. To start, I cleaned (removing an unnamed column and filling missing values for categorical variables with 'Unknown') and preprocessed (converting categorical variables into dummy variables for model compatibility).

**Classification Analysis**: For the first question, I used **Logistic Regression** to classify whether a product is recommended based on age, rating, and product categories. This model choice was influenced by the nature of the target variable (Recommended IND).

**Regression Analysis**: To explore the factors affecting the **Positive Feedback Count**, I applied **Linear Regression**, considering the same set of independent variables. This method was chosen for its ability to handle continuous outcome variables and provide insight into the relationships between features.

During the analysis, I encountered some challenges, such as feature selection and model tuning. Addressing these involved testing of different combinations of features and adjusting model parameters to optimize performance.

## Results and Interpretations
**Classification Results**: The Logistic Regression model gave a high accuracy of approximately **93.4%**, which suggests a strong connection between the selected features and the likelihood of a product being recommended. This implies that customer age, product rating, and the product categories significantly influence recommendation behavior.

**Regression Results**: The Linear Regression model, however, produced a low \(R^2\) score of about **0.015**, which implies a weak connection between these features and the Positive Feedback Count. This suggests that while some features strongly influence whether a product is recommended, they do not significantly affect the volume of positive feedback.

**Interpretation**: My analysis indicates that while age, product ratings, and categories strongly predict whether a product is recommended, they are not reliable predictors of positive feedback count. This inconsistency may suggest that while certain attributes influence recommendation likelihood, the drivers of positive feedback may include unexamined factors such as review sentiment, product quality, or customer service experiences.

## Conclusion
The findings from my project emphasize the complexity of customer feedback mechanisms in e-commerce settings. Understanding the varying relationships between product attributes and customer feedback can help retailers to tailor their strategies more effectively.
