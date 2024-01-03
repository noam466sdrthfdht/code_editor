import streamlit as st
import io
import os
import tempfile
import subprocess

def analyze_code(code):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as temp:
        # Write the code to the file
        temp.write(code)
        temp_name = temp.name

    # Run flake8 on the temporary file
    result = subprocess.run(['flake8', temp_name], text=True, capture_output=True)

    # Get the flake8 output
    flake8_output = result.stdout

    # Run black on the temporary file
    result = subprocess.run(['black', '--diff', '--quiet', temp_name], text=True, capture_output=True)

    # Get the black output
    black_output = result.stdout

    # Delete the temporary file
    if os.path.exists(temp_name):
        try:
            os.unlink(temp_name)
        except Exception as e:
            flake8_output += f"\nError deleting temporary file: {e}"

    return flake8_output, black_output

st.title('Python Code Analyzer')

code = st.text_area('Enter your Python code here:', value='', height=None, max_chars=None, key=None)

if st.button('Analyze'):
    if code:
        flake8_result, black_result = analyze_code(code)
        if flake8_result:
            st.text_area('Flake8 Analysis Result:', value=flake8_result, height=None, max_chars=None, key=None)
        if black_result:
            st.text_area('Black Formatting Suggestions:', value=black_result, height=None, max_chars=None, key=None)
    else:
        st.write('Please enter some Python code to analyze.')
