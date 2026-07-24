import pandas as pd
from sklearn.metrics import accuracy_score

# Example comparison
results = pd.DataFrame({
    "Model": [
        "Random Forest",
        "Gradient Boosting",
        "Support Vector Machine"
    ],
    "Accuracy": [
        0.90,
        0.92,
        0.89
    ]
})
results.to_csv("model_comparison.csv", index=False)
print(results)
