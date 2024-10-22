import streamlit as st
import resources.ai as ai

def pysearch():
    with st.container():
        # Get user input from the text area
        user_input = st.text_area("Please enter your question:")

        st.markdown("""
        Example questions:
        * "How can I build an API?"
        * "How can I verify a data structure?"
        * "How can I convert ISO time to human-readable time?"
        * "How do I scrape a webpage?"
        * "What should I use to handle SQL databases in Python?"
        * "How can I create a GUI for my Python application?"
        * "How can I parallelize tasks in Python?"
        * "How can I test my Python code?"
        * "What can I use to handle HTTP requests?"
        * "How do I work with machine learning in Python?"
        """)
        for question in ai.questions:
            extracted_subject = ai.extract_subject(question)
            recommended_framework = ai.python_framework_recommendation(extracted_subject)

            st.write(f"Question: {question}")
            st.write(f"Subject: {extracted_subject}")
            st.write(f"Recommended Framework: {recommended_framework}")

        
        # Check if the "Submit" button is clicked
        if st.button("Submit"):
            # Store the user input in session state for later use
            st.session_state['user_input'] = user_input
        else:
            # set the session state to empty if no input is provided
            st.session_state['user_input'] = ""
    return st.session_state['user_input']