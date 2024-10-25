import streamlit as st
import resources.ai as ai


def pysearch():
    with st.container():    
        # Display Title
        st.title("PyBites Search")
        
        # Display Example Questions
        st.markdown("""
        Example questions:
        - "How can I build an API?"
        - "How can I verify a data structure?"
        - "How can I convert ISO time to human-readable time?"
        - "How do I scrape a webpage?"
        - "What should I use to handle SQL databases in Python?"
        - "How can I create a GUI for my Python application?"
        - "How can I parallelize tasks in Python?"
        - "How can I test my Python code?"
        - "What can I use to handle HTTP requests?"
        - "How do I work with machine learning in Python?"
        """)

        # Text input
        user_input = st.text_input("Please enter your question:")

        if st.button("Submit"):
            extracted_subject = ai.extract_subject(user_input)
            recommended_framework = ai.python_framework_recommendation(extracted_subject)
            string_response = f"It looks like you are interest in {extracted_subject}, I would recommend searching {recommended_framework}"
            st.write(ai.generate_nl(string_response))