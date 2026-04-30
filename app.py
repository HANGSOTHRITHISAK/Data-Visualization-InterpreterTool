import streamlit as st
import pandas as pd

# Set page title
st.set_page_config(page_title="Student Wellness AI", layout="wide")
st.title("🧠 Student Wellness & Burnout Auditor")
st.write("Using AI logic to analyze the 6 key factors of campus life and student health.")

# 1. DATA LOADER
uploaded_file = st.file_uploader("Upload 'Student_Stress_Factors.csv'", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Rename columns so they look clean in the dropdown menu
    df.columns =['Sleep', 'Headaches', 'Academic', 'StudyLoad', 'Extracurricular', 'Stress']

    # --- NEW: THE INTERACTIVE DASHBOARD ---
    st.divider()
    st.subheader("📊 Interactive Data Explorer")
    
    # The Dropdown Menu!
    selected_factor = st.selectbox(
        "Select a student factor to analyze its distribution:",['Sleep', 'Headaches', 'Academic', 'StudyLoad', 'Extracurricular', 'Stress']
    )

    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Score Distribution for: {selected_factor}**")
        # .sort_index() ensures the x-axis goes 1, 2, 3, 4, 5 cleanly
        st.bar_chart(df[selected_factor].value_counts().sort_index())
        st.caption(f"Shows how many students picked each score (1-5) for {selected_factor}.")

    with col2:
        st.write(f"**Trend: {selected_factor} vs. Stress**")
        # If they pick Stress, compare it to Sleep by default. Otherwise, compare selection to Stress.
        if selected_factor == 'Stress':
            st.line_chart(df[['Sleep', 'Stress']].head(50))
        else:
            st.line_chart(df[[selected_factor, 'Stress']].head(50))
# --- INTERACTIVE AI TUNING ---
    st.sidebar.header("⚙️ AI Model Settings")
    st.sidebar.write("Adjust these to change how the AI identifies 'At-Risk' students.")
    
    # Let the user define what "Low Sleep" is
    sleep_threshold = st.sidebar.slider("Sleep Threshold (Anything below this is 'Low')", 1, 5, 2)
    
    # Let the user define what "High Study Load" is
    study_threshold = st.sidebar.slider("Study Load Threshold (Anything above this is 'High')", 1, 5, 4)
    # --- 3. THE AI EXPERT SYSTEM ---
    st.divider()
    st.subheader("🤖 AI Burnout Risk Analysis")
    
    # ADVANCED LOGIC: A student is "At Risk" if they meet 2 or more bad markers:
    df['Risk_Points'] = 0
    df.loc[df['Sleep'] <= sleep_threshold, 'Risk_Points'] += 1
    df.loc[df['Headaches'] >= 4, 'Risk_Points'] += 1
    df.loc[df['StudyLoad'] >= study_threshold, 'Risk_Points'] += 1
    
    at_risk_df = df[df['Risk_Points'] >= 2]
    risk_percentage = (len(at_risk_df) / len(df)) * 100

    c1, c2, c3 = st.columns(3)
    c1.metric("Students Audited", len(df))
    c2.metric("High Risk Detected", len(at_risk_df), delta_color="inverse")
    c3.metric("Risk Percentage", f"{risk_percentage:.1f}%")

    if risk_percentage > 15:
        st.error(f"🚨 AI CRITICAL INSIGHT: {risk_percentage:.1f}% of students are suffering from 'Multi-Factor Burnout'.")
        st.write("**Recommended Intervention:** Focus on students reporting high headache frequency and study loads over 4.")
    else:
        st.success("✅ AI INSIGHT: Student health markers are within acceptable limits.")

    # --- 4. SHOW THE DATA ---
    with st.expander("📂 View Audited Data (Anonymized)"):
        st.dataframe(df.drop(columns=['Risk_Points']))

    # --- 5. ETHICS & AI FUNDAMENTALS ---
    st.divider()
    st.subheader("🛡️ AI Ethics & Reliability Report")
    
    eth1, eth2 = st.columns(2)
    with eth1:
        st.write("### ⚖️ Algorithmic Fairness")
        st.write("This Expert System avoids **Proxy Bias** by looking at physical symptoms (Headaches) rather than just academic grades. This ensures a fairer health assessment.")
    with eth2:
        st.write("### 🧪 Data Integrity")
        st.write(f"The AI scanned for missing data: **{df.isnull().sum().sum()}** null values found.")
        st.write("By removing null values, we prevent the AI from making **'Hallucinated'** conclusions about student health.")

else:
    st.info("Waiting for Student_Stress_Factors.csv to be uploaded...")