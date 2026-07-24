# AI-ML-Internship-TASK2-Model-Tuning

# Heart Disease Prediction using Hyperparameter Tuning

## Project Overview

This project demonstrates model selection and hyperparameter optimization for heart disease prediction using Machine Learning. Multiple classification algorithms were trained, tuned, and compared to identify the best-performing model.

The project implements:

- Random Forest Classifier
- Gradient Boosting Classifier
- Support Vector Machine (SVM)

Hyperparameter optimization was performed using GridSearchCV and RandomizedSearchCV.

## Dataset

The project uses the Heart Disease dataset.

Target Variable:

- 0 → No Heart Disease
- 1 → Heart Disease

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

## Project Workflow

1. Import Libraries
2. Load Dataset
3. Data Exploration
4. Data Cleaning
5. Train-Test Split
6. Feature Scaling
7. Random Forest Model
8. Random Forest Hyperparameter Tuning
9. Gradient Boosting Model
10. Gradient Boosting Hyperparameter Tuning
11. Support Vector Machine Model
12. SVM Hyperparameter Tuning
13. Model Comparison
14. Best Model Selection
15. Save Best Model

## Machine Learning Algorithms

- Random Forest
- Gradient Boosting
- Support Vector Machine (SVM)

## Hyperparameter Optimization

### GridSearchCV

Used for:
- Random Forest
- Support Vector Machine

### RandomizedSearchCV

Used for:
- Gradient Boosting

## Evaluation Metrics

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

## Results

Three different machine learning algorithms were trained and optimized using hyperparameter tuning.
The best-performing model was selected based on Accuracy, Precision, Recall, and F1 Score and saved using Joblib.
