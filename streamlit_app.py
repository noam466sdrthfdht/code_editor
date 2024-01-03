import streamlit as st
import subprocess

def analyze_code(user_code):
    try:
        # Write the user code to a temporary file
        with open("temp_code.py", "w") as f:
            f.write(user_code)

        # Run Coala on the temporary file
        result = subprocess.run(["coala", "--json", "--option", "coafile.yml", "temp_code.py"], capture_output=True)

        # Parse and display Coala results
        output = result.stdout.decode("utf-8")
        st.json(output)

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
