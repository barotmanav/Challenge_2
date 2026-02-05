import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyDTnzQ9utqb0nEZ8jWtnlL3b7QncB2hKiA"
genai.configure(api_key=GOOGLE_API_KEY)

print("Listing available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)
except Exception as e:
    print(f"Error: {e}")
