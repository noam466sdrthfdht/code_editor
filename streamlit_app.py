import streamlit as st
import pylint.lint
import pylint.reporters.text
import io
import sys


import tempfile



def analyze_code(code):
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.py') as temp:
        # Write the code to the file
        temp.write(code)
        temp_name = temp.name

    # Redirect stdout to a string
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()

    # Run pylint on the temporary file
    pylint.lint.Run([temp_name], reporter=pylint.reporters.text.TextReporter(sys.stdout), exit=False)

    # Get the pylint output
    output = sys.stdout.getvalue()

    # Restore stdout
    sys.stdout = old_stdout

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
