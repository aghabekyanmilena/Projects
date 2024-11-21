## Logistic Regression Model for Interview Acceptance Prediction
## Overview
This project implements a logistic regression model to predict whether a candidate will be accepted for an interview based on various features. The dataset includes information such as business travel frequency, marital status, overtime status, and gender. The model is trained and evaluated using Python's scikit-learn library.

## Dataset
The dataset used in this project is assumed to be named logatta.csv and contains the following columns:

BusinessTravel
MaritalStatus
OverTime
Gender
accepted for the interview (target variable)
The dataset is preprocessed to handle categorical variables and missing values, and then split into training and testing sets.

## Results
After training, the model's performance is evaluated using accuracy and other classification metrics. The following metrics are reported:

Accuracy
Precision
Recall
F1-Score
Additionally, the ROC curve and AUC score provide insight into the model's ability to distinguish between classes.