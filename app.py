import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyB92k02wczwkOK3VWuLQZ5JyJWj-uAV6Tk")

def review_code(code):
    """Send the code to Google Gemini AI API and get the review response."""
    model = genai.GenerativeModel("gemini-pro")  
    prompt = f"""
    Analyze the following Python code for correctness. 
    If there are no issues, simply return 'No issues found.' 
    If there are issues, provide:
    1. A list of potential bugs or errors.
    2. A corrected version of the code.

    ```python
    {code}
    ```
    """
    response = model.generate_content(prompt)
    return response.text if hasattr(response, "text") else response

st.title("An AI Code Reviewer")
st.write("Enter your Python code here ...")

code_input = st.text_area("Python Code:", height=200)

if st.button("Generate"):
    if code_input.strip():
        with st.spinner("Analyzing code..."):
            review_result = review_code(code_input)

        if "No issues found." in review_result:
            st.success("Your code is correct! No changes needed.")
        else:
            st.subheader("Code Review")
            st.markdown("### **Bug Report**")
            st.write(review_result.split("Fixed Code:")[0])  
            st.markdown("### **Fixed Code**")
            st.code(review_result.split("Fixed Code:")[-1], language="python")  

    else:
        st.warning("Please enter some Python code to review!")
