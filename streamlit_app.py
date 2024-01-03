import streamlit as st
import subprocess
import json

def analyze_code(user_code):
    try:
        # Write the user code to a temporary file
        with open("temp_code.py", "w") as f:
            f.write(user_code)

        # Run Coala on the temporary file
        result = subprocess.run(["coala", "--json", "--option", "coafile.yml", "temp_code.py"], capture_output=True)

        # Display raw output for debugging
        st.text("Raw Output:")
        st.text(result.stdout.decode("utf-8"))

        # Check if the output is not empty before parsing as JSON
        if result.stdout:
            # Parse and display Coala results
            output = json.loads(result.stdout.decode("utf-8"))
            st.json(output)
        else:
            st.warning("Coala output is empty.")

    except Exception as e:
        st.error(f"Error analyzing code: {e}")

def main():
    st.title("Code Analyzer App")

    # Text area for code input
    user_code = st.text_area("Write your code here", height=300)

    # Button to analyze code
    if st.button("Analyze Code"):
        analyze_code(user_code)

if __name__ == "__main__":
    main()
