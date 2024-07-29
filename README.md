# AI Coding Helper

This project is an AI-powered coding assistant that suggests code, helps debug, and provides tips to improve your code. It uses Gemini AI to provide intelligent suggestions and feedback.

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/ai_coding_helper.git
    cd ai_coding_helper
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Gemini API key:
    - Replace `'YOUR_GEMINI_API_KEY'` in `app/ai_model.py` with your actual Gemini API key.

4. Run the Streamlit app:
    ```bash
    streamlit run app/streamlit_app.py
    ```

5. Open your browser and go to the URL provided by Streamlit to use the AI Coding Helper.

## Features

- **Suggest Code**: Suggests the next lines of code based on the current code.
- **Help Debug**: Identifies and fixes errors in the code.
- **Give Tips**: Provides tips to improve the code quality.

## License

This project is licensed under the MIT License.
