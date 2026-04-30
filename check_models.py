import google.generativeai as genai

# --- IMPORTANT ---
# Paste your actual Gemini API key here
API_KEY = "AIzaSyAQkyZO7WbJUI3o4l1fuWAeRgDc0XP-Slw" 

try:
    genai.configure(api_key=API_KEY)

    print("✅ Successfully connected. Available models for your API key:")
    print("---------------------------------------------------------")

    for model in genai.list_models():
        # We only care about models that can actually generate text
        if 'generateContent' in model.supported_generation_methods:
            print(f"- {model.name}")

except Exception as e:
    print(f"❌ An error occurred: {e}")