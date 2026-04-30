# FILE: api_version.py (The "Failed" Gemini Experiment - Final Version)

import streamlit as st
import pandas as pd
from google import genai

st.set_page_config(page_title="API Experiment", layout="centered")
st.title("🧪 Initial Prototype: Gemini API")
st.write("This version attempts to use a cloud-based LLM to interpret the data.")

# --- CONFIGURATION (Remember to add your key) ---
try:
    client = genai.Client(api_key="[INSERT YOUR GEMINI KEY HERE]")
except Exception as e:
    st.error("API Key not found or invalid. Please check your configuration.")
    st.stop()

# --- DATA LOADER ---
uploaded_file = st.file_uploader("Upload 'Student_Stress_Factors.csv'", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns =['Sleep', 'Headaches', 'Academic', 'StudyLoad', 'Extracurricular', 'Stress']
    st.dataframe(df.head())

    # --- AI INTERPRETER ---
    st.subheader("🤖 Ask the AI a question")
    user_query = st.text_input("e.g., What is the main cause of stress?")

    if user_query:
        summary_stats = df.describe().to_string()
        prompt = f"Context: {summary_stats} \nQuestion: {user_query}. Answer in one friendly sentence."

        with st.spinner("Contacting Google's AI Servers..."):
            try:
                # We use the EXACT model name we discovered from our test script
                response = client.models.generate_content(
                    model='models/gemini-2.5-flash', # This is guaranteed to be a valid name
                    contents=prompt
                )
                st.success(f"AI Interpretation: {response.text}")

            except Exception as e:
                # Any error now is almost certainly a server overload (503) or a rate limit.
                st.error("🚨 LIVE API ERROR: Could not get a response from the AI model.")
                st.warning("This unreliability (likely due to server traffic on the free tier) is why we pivoted to a local Expert System for the final version.")
                st.code(f"Error Details: {e}")
else:
    st.info("Upload the CSV to attempt a connection to the Gemini API.")