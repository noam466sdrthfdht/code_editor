import streamlit as st
import pylint.lint
import pylint.reporters.text
import io
import sys

def analyze_code(code):
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    pylint.lint.Run([code], reporter=pylint.reporters.text.TextReporter(sys.stdout), exit=False)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output

st.title('Python Code Analyzer')

code = st.text_area('Enter your Python code here:', value='', height=None, max_chars=None, key=None)

if st.button('Analyze'):
    if code:
        result = analyze_code(code)
        st.text_area('Analysis Result:', value=result, height=None, max_chars=None, key=None)
    else:
        st.write('Please enter some Python code to analyze.')
