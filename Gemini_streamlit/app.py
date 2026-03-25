#WEBSITE USING STREAMLIT CODE GOES HERE
import streamlit as st
from main import gemini_llm

st.title("Gemini LLM tool")
st.subheader("Generate content with gemini")
user_input=st.text_area(
    "Enter your prompt..",
    placeholder="what is the theory of relativity"
)
if st.button("Generate content"):
    if user_input.strip()=="":
        st.warning("Enter valid prompt")
    else:
        with st.spinner("Generating content:..."):
            answer=gemini_llm(user_input)
            st.success('content Generated....')
            st.write(answer)