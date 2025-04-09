Phishing Email Classifier (ML + Streamlit)
- A machine learning-based web app that classifies emails as **No**, **Low**, **Moderate**, **High**, or **Critical** risk based on four key phishing indicators. 
- Built using a Multilayer Perceptron (MLP) and deployed using Streamlit.

Features
- Accepts 4 input features:
  - Domain reputation
  - URL structure
  - Sensitive content in body
  - Suspicious keywords
- Trained using **MLPClassifier** with **97.85% accuracy**
- Balanced using **SMOTE** for better class representation
- 10-fold cross-validation + RMSE evaluation
- Deployed as an interactive and user-friendly Streamlit app

Model Training
- Preprocessed a custom phishing dataset with categorical labels
- Used `sklearn`'s `MLPClassifier` for training
- Applied SMOTE from `imblearn` to handle class imbalance
- Evaluated with:
  - Accuracy: 97.85%
  - Root Mean Square Error (RMSE): 0.1466
  - Cross-validation Accuracy: 98.64%
