import google.generativeai as genai

# Set up API key directly
api_key = 'AIzaSyASy8RA397eN5yFSD2EfuKDgDZ64b5IawA'
genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

def suggest_code(user_code):
    prompt = f"Suggest the next lines of code for the following code:\n{user_code}"
    response = model.generate_content(prompt)
    return response.text.strip()

def debug_code(user_code):
    prompt = f"Find and fix the error in the following code:\n{user_code}"
    response = model.generate_content(prompt)
    return response.text.strip()

def give_tips(user_code):
    prompt = f"Give tips to improve the following code:\n{user_code}"
    response = model.generate_content(prompt)
    return response.text.strip()
