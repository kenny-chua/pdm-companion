import streamlit as st


import resources.ai as ai

# import pybites_search - this doesn't work?
from pybites_search.all_content import AllSearch


def bobsearch():
    with st.container():
        # Display Title
        st.title("Bob's Search")

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

            # Change extracted_subject from list to string
            # Method 1
            if isinstance(extracted_subject, list):
                extracted_subject = extracted_subject[0]
            
            # Method 2
            # if isinstance(extracted_subject, list):
            #     extracted_subject = ' '.join(extracted_subject)

            # Instantiate bob's object
            searcher = AllSearch()
            results = searcher.match_content(extracted_subject)
            if results:
                for result in results:
                    st.markdown(f"### [{result.title}]({result.url})")
            else:
                st.write("No results found.")
