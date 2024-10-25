import marvin

questions = [
    "How do I work with machine learning in Python?",
    "How can I build an API?",
    "How can I verify a data structure?",
    "How can I convert ISO time to human-readable time?",
    "How do I scrape a webpage?",
    "What should I use to handle SQL databases in Python?",
    "How can I create a GUI for my Python application?",
    "How can I parallelize tasks in Python?",
    "How can I test?",
    "What can I use to handle HTTP requests?",
    "How do I work with machine learning in Python?",
]


# Extract Topic
def extract_subject(question):
    subject = marvin.extract(
        question,
        instructions="From the question: {{ question }}, extract the main subject. Limit to 1.",
    )
    return subject


# Recommend Framework
@marvin.fn
def python_framework_recommendation(extracted_subject: str):
    """
    Recommend the most suitable Python framework or Module based on {{ extracted_subject }}. Just return the framework.
    """


# Natural Language Generation
@marvin.fn
def generate_nl(input: str):
    """
    With {{ input }}, rewrite sentence with correct grammar, punctuation and sentence structure. Remove any symbols, for example brackets and quotes that are not needed in a regular english sentence.
    """
