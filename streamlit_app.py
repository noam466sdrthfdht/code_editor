import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function for AI text generation using GPT-2
def ai_code_completion(user_code):
    try:
        # Make a request to the OpenAI API for text generation using GPT-2
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=user_code,
            max_tokens=100  # Adjust as needed
        )
        completed_code = response.choices[0].text.strip()
    except Exception as e:
        st.error(f"Error during AI code completion: {e}")
        completed_code = user_code

    return completed_code

def main():
    st.title("Real-Time Collaborative Code Editor with AI Code Completion")

    # Text area for code input
    user_code = st.text_area("Write your code here", height=300)

    # Simulate AI code completion
    completed_code = ai_code_completion(user_code)

    # Display the completed code
    st.text("Completed Code:")
    st.code(completed_code, language='python')

if __name__ == "__main__":
    main()
