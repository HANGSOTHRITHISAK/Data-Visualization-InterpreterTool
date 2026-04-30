 code Markdown

# 🧠 Student Wellness & Burnout Auditor

A functional prototype of a **Symbolic AI Expert System** built for an AI Fundamentals course. This tool audits campus wellness data across 6 factors to predict and analyze student burnout risks.

## 🚀 Project Overview
This application addresses the niche problem of student mental health by analyzing physiological and academic markers. Unlike generic AI chatbots, it uses a transparent, rule-based expert system to identify "at-risk" students, ensuring 100% reliability and explainability.

### Key Features:
*   **Interactive Dashboard:** Visualize distributions and trends for Sleep, Headaches, and Study Load.
*   **AI Expert System:** A multi-factor risk engine that identifies burnout clusters.
*   **Interactive Tuning:** Real-time sliders allow users to adjust the AI's sensitivity thresholds.
*   **Ethics Audit:** Built-in scans for data integrity and algorithmic bias.

## 🛠️ Installation & Setup

To run this app locally, ensure you have Python installed, then follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

2. Install Dependencies

Install the required libraries using pip:
code Bash

pip install streamlit pandas

3. Launch the Application

Run the Streamlit server:
code Bash

streamlit run app.py

4. Upload Data

Once the browser window opens, upload the provided file: Student_Stress_Factors.csv.
🛡️ AI Fundamentals & Ethics

This project was developed with a focus on Explainable AI (XAI).

    Reliability: By using a Symbolic AI approach rather than a cloud-based LLM, the tool avoids 503 server errors and maintain high availability.

    Transparency: The logic used to flag "High Risk" students is fully visible and adjustable, preventing "Black Box" decision-making.

    Data Quality: The system scans for null values to prevent hallucinations and analyzes demographic distribution to mitigate bias.

👤 Author

    [Your Name] - Solo Developer - AI Fundamentals Course
