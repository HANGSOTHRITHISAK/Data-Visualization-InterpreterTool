# 🧠 Student Wellness & Burnout Auditor

A functional prototype of a **Symbolic AI Expert System** built for an AI Fundamentals course. This tool audits campus wellness data across 6 key factors to identify, analyze, and predict student burnout risks.

## 🚀 Project Overview
This application addresses the specific niche problem of student mental health and academic burnout. Instead of using a "Black Box" generative AI, this tool implements an **Explainable AI (XAI)** approach using a rule-based expert system. This ensures the tool is 100% reliable, works offline, and provides transparent reasoning for every risk assessment.

### Key Features:
*   **Interactive Dashboard:** Users can toggle between 6 data factors (Sleep, Headaches, Academic Performance, Study Load, Extracurriculars, and Stress) to see real-time distributions.
*   **AI Expert System:** A multi-factor risk engine that identifies "High-Risk" burnout clusters by weighing physiological and academic markers.
*   **Interactive AI Tuning:** Features a sidebar with sliders that allow users to tune the AI model's sensitivity (e.g., adjusting the threshold for "Low Sleep").
*   **Ethics & Integrity Audit:** Built-in scans for missing data and demographic bias to ensure the AI's conclusions are fair and accurate.

## 🛠️ How to Run the Project

Follow these steps to run the prototype on your local machine:

### 1. Install Required Libraries
Open your terminal or command prompt and run:
```bash
pip install streamlit pandas
