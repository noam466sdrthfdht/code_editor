import streamlit as st
import os
import tempfile
import subprocess
import black

def analyze_code(code):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as temp:
        # Write the code to the file
        temp.write(code)
        temp_name = temp.name



    # If there are no flake8 errors, format the code using black

    try:
        with open(temp_name, 'r+') as f:
            code = f.read()
            f.seek(0)
            f.write(black.format_str(code, mode=black.FileMode()))
            f.truncate()

        with open(temp_name, 'r') as f:
            black_output = f.read()

    except Exception as e:
        black_output = f"\nError formatting code: {e}"


    # Delete the temporary file
    if os.path.exists(temp_name):
        try:
            os.unlink(temp_name)
        except Exception as e:
            black_output += f"\nError deleting temporary file: {e}"

    return black_output

st.title('Python Code Analyzer')

code = st.text_area('Enter your Python code here:', value='', height=None, max_chars=None, key=None)

if st.button('Analyze'):
    if code:
        black_result = analyze_code(code)

        if black_result:
            st.text_area('Formatted Code:', value=black_result, height=None, max_chars=None, key=None)
    else:
        st.write('Please enter some Python code to analyze.')
