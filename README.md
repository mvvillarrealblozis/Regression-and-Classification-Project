# BUS316-Final-Project Report

## Central Research Question
The core focus of this project was to analyze a Women’s Clothing E-Commerce dataset to understand the relationship between product reviews and customer recommendations, as well as to explore factors influencing the positive feedback count. Specifically, I aimed to answer two critical questions:

1. **Is there a connection between a customer's age, the product rating, and specific product categories (Department Name and Class Name) with whether a product is recommended (Recommended IND)?**
2. **Do these same variables have a connection with the positive feedback count received on a review?**

By answering these questions, my work contributes to a deeper understanding of customer behavior and satisfaction factors, ultimately aiding in enhancing product recommendations and marketing strategies.

## Solution Approach
To address the outlined research questions, I employed a two-pronged analytical approach: **Classification and Regression**.

**Data Preprocessing**: The dataset comprises 23,486 rows and 10 feature variables. Initial data exploration involved cleaning (removing an unnamed column and filling missing values for categorical variables with 'Unknown') and preprocessing (converting categorical variables into dummy variables for model compatibility).

**Classification Analysis**: For the first research question, I utilized **Logistic Regression** to classify whether a product is recommended based on age, rating, and product categories. This model choice was driven by the binary nature of our target variable (Recommended IND).

**Regression Analysis**: To explore the factors affecting the **Positive Feedback Count**, I applied **Linear Regression**, considering the same set of independent variables. This method was chosen for its ability to handle continuous outcome variables and provide insight into the relationships between features.

During the analysis, I encountered challenges, particularly in feature selection and model tuning. Addressing these involved rigorous testing of different combinations of features and adjusting model parameters to optimize performance.

## Results and Interpretations
**Classification Results**: The Logistic Regression model demonstrated a high accuracy of approximately **93.4%**, suggesting a strong connection between the selected features and the likelihood of a product being recommended. This indicates that customer age, product rating, and the product categories significantly influence recommendation behavior.

**Regression Results**: The Linear Regression model, however, yielded a low \(R^2\) score of about **0.015**, indicating a weak connection between these features and the Positive Feedback Count. This suggests that while certain features strongly influence whether a product is recommended, they do not significantly affect the volume of positive feedback.

**Interpretation**: My analysis indicates that while age, product ratings, and categories strongly predict whether a product is recommended, they are not reliable predictors of positive feedback count. This discrepancy may suggest that while certain attributes influence recommendation likelihood, the drivers of positive feedback may include unexamined factors such as review sentiment, product quality, or customer service experiences.

## Conclusion
The findings from my project underscore the complexity of customer feedback mechanisms in e-commerce settings. Understanding the nuanced relationships between product attributes and customer feedback can empower retailers to tailor their strategies more effectively. For future work, incorporating text analysis of review bodies and exploring additional customer interaction metrics could provide further insights into driving positive customer feedback.
