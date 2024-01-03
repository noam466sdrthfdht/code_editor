import streamlit as st
import io
import sys
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
    output = result.stdout

    # Delete the temporary file
    if os.path.exists(temp_name):
        try:
            os.unlink(temp_name)
        except Exception as e:
            output += f"\nError deleting temporary file: {e}"

    return output

st.title('Python Code Analyzer')

code = st.text_area('Enter your Python code here:', value='', height=None, max_chars=None, key=None)

if st.button('Analyze'):
    if code:
        result = analyze_code(code)
        st.text_area('Analysis Result:', value=result, height=None, max_chars=None, key=None)
    else:
        st.write('Please enter some Python code to analyze.')
