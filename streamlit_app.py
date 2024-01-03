import streamlit as st
from openai import OpenAI

# Set your OpenAI API key

client = OpenAI(
    # This is the default and can be omitted
    api_key="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"
)
# Function for AI text generation using GPT-2
def ai_code_completion(user_code):
    try:
        # Make a request to the OpenAI API for text generation using GPT-2


        response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_code,
            }
        ],
        model="davinci-codex",
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
