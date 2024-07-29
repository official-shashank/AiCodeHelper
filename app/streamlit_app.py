import sys
import os
import streamlit as st

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ai_model import suggest_code, debug_code, give_tips

# Streamlit app layout
st.title('AI Coding Helper')
st.write("This tool suggests code, helps debug, and provides tips to improve your code using Google Generative AI.")

# Text area for user to input their code
user_code = st.text_area("Enter your code here:", height=200)

# Buttons to trigger AI functionalities
if st.button("Suggest Code"):
    suggestion = suggest_code(user_code)
    st.subheader("Suggested Code:")
    st.code(suggestion, language='python')

if st.button("Debug Code"):
    debug_suggestion = debug_code(user_code)
    st.subheader("Debugged Code:")
    st.code(debug_suggestion, language='python')

if st.button("Get Tips"):
    tips = give_tips(user_code)
    st.subheader("Tips:")
    st.text(tips)
