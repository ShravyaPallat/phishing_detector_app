import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("mlp_phishing_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit UI
st.title("🔎 Phishing Email Classifier")

st.markdown("""
### How It Works:
Enter values (0, 0.5, 1) for the email factors, and the model will classify the email risk level.
- **0** → Feature not present  
- **0.5** → Feature partially present  
- **1** → Feature strongly present  
""")

# User Inputs
domain = st.selectbox("📌 Domain Reputation:", [0, 0.5, 1])
url = st.selectbox("🌐 URL Analysis:", [0, 0.5, 1])
sensitive_info = st.selectbox("🔑 Sensitive Info Requests:", [0, 0.5, 1])
suspicious_words = st.selectbox("⚠️ Suspicious Keywords:", [0, 0.5, 1])

# Prediction function
def classify_email(domain, url, sensitive_info, suspicious_words):
    features = np.array([[domain, url, sensitive_info, suspicious_words]])
    prediction = model.predict(features)[0]

    classification_mapping = {
        0: "No Risk ✅",
        1: "Low Risk ⚠️",
        2: "Moderate Risk ⚠️",
        3: "High Risk 🚨",
        4: "Critical Risk 🚨⚠️"
    }
    return classification_mapping.get(prediction, "Unknown")

# Predict Button
if st.button("🔍 Classify Email"):
    result = classify_email(domain, url, sensitive_info, suspicious_words)
    st.markdown(f"### 🔎 Classification: **{result}**")

    # Additional information based on classification
    info = {
        "No Risk ✅": "✅ This email is safe and does not show phishing characteristics.",
        "Low Risk ⚠️": "⚠️ This email has minor phishing indicators. Proceed with caution.",
        "Moderate Risk ⚠️": "⚠️ This email shows some phishing signs. Verify sender and links before interacting.",
        "High Risk 🚨": "🚨 Strong phishing indicators detected! Do not click on any links or provide sensitive information.",
        "Critical Risk 🚨⚠️": "🚨⚠️ Highly suspicious email! Most likely a phishing attempt. Delete immediately."
    }

    st.info(info.get(result, "❓ Classification not recognized."))

# Footer
st.markdown("---")
st.markdown("🚀 **Developed by Your Team** | Powered by Streamlit & Machine Learning")
