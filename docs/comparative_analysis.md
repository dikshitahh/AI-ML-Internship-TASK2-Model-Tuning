# Comparative Analysis Report

## Objective

The objective of this project was to identify the best machine learning model for heart disease prediction through model selection and hyperparameter optimization.

## Models Evaluated

### 1. Random Forest

Hyperparameter Optimization:
- GridSearchCV

Advantages:
- Handles non-linear relationships
- Robust to overfitting
- Good feature importance

Disadvantages:
- Slightly longer training time

### 2. Gradient Boosting

Hyperparameter Optimization:

- RandomizedSearchCV

Advantages:

- High predictive accuracy
- Handles complex patterns
- Strong ensemble learning technique

Disadvantages:
- Higher computational cost

### 3. Support Vector Machine

Hyperparameter Optimization:
- GridSearchCV

Advantages:
- Effective for binary classification
- Performs well after feature scaling

Disadvantages:
- Slower for larger datasets

## Performance Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score

The evaluation results were saved in:    model_comparison.csv

## Final Model Selection

The final model was selected based on:

- Highest Accuracy
- Highest F1 Score
- Generalization Performance
- Model Complexity

The selected model was saved using Joblib for future predictions.

## Conclusion

Hyperparameter tuning significantly improved model performance compared to the baseline models.
GridSearchCV and RandomizedSearchCV efficiently identified better parameter combinations, resulting in improved classification performance.
