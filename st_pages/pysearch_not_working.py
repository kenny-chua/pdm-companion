import streamlit as st
import resources.ai as ai

def pysearch():
    # Initialize session state
    # if 'ai_response' not in st.session_state:
    #     st.session_state.ai_response = ""
    # if 'user_input' not in st.session_state:
    #     st.session_state.user_input = ""

    if st.session_state.get('Clear'):
        st.session_state['user_input'] = ""
    
    # Function to handle submit action
    def on_submit():
        if st.session_state.user_input:
            extracted_subject = ai.extract_subject(st.session_state.user_input)
            recommended_framework = ai.python_framework_recommendation(extracted_subject)
            string_response = (f"It looks like you are interest in {extracted_subject}, I would recommend searching {recommended_framework}")
            st.session_state.ai_response = ai.generate_nl(string_response)

    # Function to handle clear action
    def on_clear():
        st.session_state.user_input = ""
        st.session_state.ai_response = ""

    # Display Example Questions
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

    # Text input
    st.text_input("Please enter your question:", key='user_input')

    # Display AI Response if populated
    if st.session_state.ai_response:
        st.write(st.session_state.ai_response)

    # Buttons in a side-by-side layout
    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        st.button("Submit", on_click=on_submit)
    with col2:
        st.button("Clear", on_click=on_clear)