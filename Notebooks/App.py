import streamlit as st
import pickle
import pandas as pd
import numpy as np
from transformers import pipeline
from streamlit_option_menu import option_menu  # For a better navigation menu
from urllib.parse import quote  # For URL encoding

# Customizing UI Theme
st.set_page_config(page_title="AI Insurance App", page_icon="📊", layout="wide")

# Custom CSS for styling (pink background)
st.markdown("""
<style>
    /* Pink background for the entire page */
    body {
        background-color: #FF69B4;
    }
    /* Main content area background */
    .stApp {
        background-color: #FFE6EE;  /* Light pink for contrast */
        padding: 20px;
        border-radius: 10px;
        margin: 20px;
    }
    /* Button styling */
    .stButton>button {
        background-color: #FF1493;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #FF69B4;
    }
    /* Input field styling */
    .stTextInput>div>div>input {
        border-radius: 5px;
        padding: 10px;
    }
    /* Headings */
    .stMarkdown h1 {
        text-align: center;
        color: #FF1493;
    }
    .stMarkdown h2 {
        color: #FF1493;
    }
    .stMarkdown h3 {
        color: #FF1493;
    }
    /* Success and error messages */
    .stSuccess {
        background-color: #FFE6EE;
        color: #FF1493;
        padding: 10px;
        border-radius: 5px;
    }
    .stError {
        background-color: #FFE6EE;
        color: #FF1493;
        padding: 10px;
        border-radius: 5px;
    }
    /* Social media icons */
    .social-icons {
        text-align: center;
        margin-top: 20px;
    }
    .social-icons a {
        margin: 0 10px;
    }
    .social-icons img {
        width: 40px;
        height: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Load trained models
model_files = {
    "Insurance Risk Prediction": "random_forest_regressor.pkl",
}

# Load models dynamically
models = {}
for name, path in model_files.items():
    try:
        with open(path, "rb") as f:
            models[name] = pickle.load(f)
    except Exception as e:
        st.error(f"❌ Error loading {name}: {e}")

# Load the chatbot model
@st.cache_resource
def load_chatbot():
    chatbot = pipeline("text-generation", model="gpt2")  # Replace with "microsoft/DialoGPT-medium" for a conversational model
    return chatbot

chatbot = load_chatbot()

# Homepage
def homepage():
    st.markdown("<h1>🌟 Welcome to the AI-Powered Insurance Dashboard 🌟</h1>", unsafe_allow_html=True)
    st.write("""
    **👋 Welcome!** This dashboard is designed to help you streamline insurance processes using cutting-edge AI and machine learning technologies. Whether you're assessing risk, predicting claims, or seeking quick answers to insurance-related queries, this tool has you covered.

    ### 🛠️ How to Use This Webpage:
    1. **📊 Insurance Risk Prediction**:
       - Navigate to the "Insurance Risk Prediction" section from the sidebar.
       - Enter customer details such as age, income, claim history, and more.
       - Click "🚀 Predict Risk Level" to get an instant risk classification (High Risk or Low Risk).

    2. **🤖 AI-Powered Chatbot**:
       - Navigate to the "Chatbot" section from the sidebar.
       - Ask any insurance-related questions, and the chatbot will provide concise and accurate answers.

    ### 💡 Why Choose This Tool?
    - **⚡ Efficiency**: Automate risk assessment and claim prediction.
    - **🎯 Accuracy**: Leverage advanced AI models for reliable results.
    - **😊 User-Friendly**: Simple and intuitive interface for seamless navigation.

    Get started by selecting a task from the sidebar!
    """)

# Sidebar for navigation using option_menu
with st.sidebar:
    selected = option_menu(
        menu_title="🔍 Navigation",
        options=["Home", "Insurance Risk Prediction", "Chatbot"],
        icons=["house", "shield", "robot"],
        menu_icon="cast",
        default_index=0,
    )

# Display selected page
if selected == "Home":
    homepage()

# 🎯 TASK 1: Insurance Risk Prediction
elif selected == "Insurance Risk Prediction":
    st.subheader("🛡️ Insurance Risk Prediction")
    
    # User Inputs
    col1, col2 = st.columns(2)
    with col1:
        customer_age = st.number_input("📌 Customer Age", min_value=18, max_value=100)
        annual_income = st.number_input("💰 Annual Income ($)", min_value=10000, max_value=200000)
        vehicle_property_age = st.number_input("🚗 Vehicle/Property Age", min_value=0, max_value=50)
    with col2:
        claim_history = st.number_input("🔄 Claim History", min_value=0, max_value=10)
        fraudulent_claim = st.number_input("🚨 Fraudulent Claim (0 or 1)", min_value=0, max_value=1)
        premium_amount = st.number_input("💲 Premium Amount ($)", min_value=0, max_value=100000)
    risk_score = st.number_input("🎯 Risk Score", min_value=0, max_value=100)

    # One-Hot Encoding for Policy Type
    policy_type = st.selectbox("📜 Policy Type", ["Auto", "Health", "Life", "Property"])
    policy_encoded = {
        "Policy_Auto": int(policy_type == "Auto"),
        "Policy_Health": int(policy_type == "Health"),
        "Policy_Life": int(policy_type == "Life"),
        "Policy_Property": int(policy_type == "Property"),
    }

    # One-Hot Encoding for Gender
    gender = st.selectbox("⚤ Gender", ["Male", "Female", "Other"])
    gender_encoded = {
        "Gender_Male": int(gender == "Male"),
        "Gender_Female": int(gender == "Female"),
        "Gender_Other": int(gender == "Other"),
    }

    # Generate Anomaly Detection Features
    anomaly_if = 0.5  # Placeholder
    anomaly_ae = 0.2  # Placeholder
    fraud_anomaly_tag = 1 if claim_history > 3 else 0

    # Get expected feature names from the model
    expected_features = models[selected].feature_names_in_

    # Create input_data dictionary
    input_data_dict = {
        "Customer_Age": customer_age,
        "Annual_Income": annual_income,
        "Vehicle_Property_Age": vehicle_property_age,
        "Claim_History": claim_history,
        "Fraudulent_Claim": fraudulent_claim,
        "Premium_Amount": premium_amount,
        "Risk_Score": risk_score,
        "Policy_Auto": policy_encoded["Policy_Auto"],
        "Policy_Health": policy_encoded["Policy_Health"],
        "Policy_Life": policy_encoded["Policy_Life"],
        "Policy_Property": policy_encoded["Policy_Property"],
        "Gender_Male": gender_encoded["Gender_Male"],
        "Gender_Female": gender_encoded["Gender_Female"],
        "Gender_Other": gender_encoded["Gender_Other"],
        "Anomaly_IF": anomaly_if,
        "Anomaly_AE": anomaly_ae,
        "Fraud_Anomaly_Tag": fraud_anomaly_tag,
    }

    # Ensure input data follows the exact order expected by the model
    input_data = pd.DataFrame([[input_data_dict[feature] for feature in expected_features]], columns=expected_features)

    # Predict Risk Level
    if st.button("🚀 Predict Risk Level"):
        with st.spinner("Predicting..."):
            try:
                prediction = models[selected].predict(input_data)
                risk_label = "🔴 High Risk" if prediction[0] else "🟢 Low Risk"
                st.success(f"✅ Prediction: {risk_label}")
                st.balloons()  # Show balloons animation
            except Exception as e:
                st.error(f"❌ Error during prediction: {e}")

# 🎯 TASK 2: Chatbot
elif selected == "Chatbot":
    st.subheader("🤖 AI-Powered Insurance Chatbot")

    st.write("""
    Ask me anything about insurance policies, claims, or general queries!
    """)

    # Input for user query
    user_input = st.text_input("You:", "")

    if st.button("Search Query"):
        if user_input.strip() != "":
            with st.spinner("Generating response..."):
                try:
                    # Generate chatbot response with a max_length of 150 tokens
                    chatbot_response = chatbot(
                        user_input,
                        max_length=150,  # Limit response length
                        num_return_sequences=1,
                        truncation=True  # Ensure the response is truncated if it exceeds max_length
                    )[0]['generated_text']

                    # Truncate the response to approximately 150 words
                    words = chatbot_response.split()
                    truncated_response = " ".join(words[:150])  # Keep the first 150 words
                    st.write(f"**Chatbot:** {truncated_response}")
                    st.balloons()  # Show balloons animation

                    # Social Media Sharing Icons
                    encoded_note = quote(truncated_response)  # URL encode the response
                    st.markdown(
                        f"""
                        <div class="social-icons">
                            <p style="text-align:center; font-size:18px; font-weight:bold; color:#800020;">
                            Share Your Query
                            </p>
                            <a href="https://api.whatsapp.com/send?text={encoded_note}" target="_blank">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" alt="WhatsApp">
                            </a>
                            <a href="https://www.instagram.com/" target="_blank">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram">
                            </a>
                            <a href="https://www.facebook.com/sharer/sharer.php?u={encoded_note}" target="_blank">
                                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/Facebook_icon.svg" alt="Facebook">
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                except Exception as e:
                    st.error(f"❌ Error generating response: {e}")
                    
                    
# Footer
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>🚀 Developed by <b>GUVI Geek Network Private Limited</b> | AI for Insurance Innovation</p>",
    unsafe_allow_html=True
)
