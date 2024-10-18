import marvin

from play_text import questions
marvin.settings.openai.api_key = 'sk-proj-qyw18WnAby266IKbQvIIT3BlbkFJXb1kEvR4467lNK4sFKh7'

def extraction_comparison(questions:list):
    # Initialize empty dictionary
    extraction_results = []

    # Loop through potential extraction words
    for question in questions:
        what_word_to_use = {
            "topics": marvin.extract(question, instructions="Retrieve topics"),
            "technology": marvin.extract(question, instructions="Retrieve technologies"),
            "concepts": marvin.extract(question, instructions="Retrieve concepts"),
            "subjects": marvin.extract(question, instructions="Retrieve subjects"),
            "skills": marvin.extract(question, instructions="Retrieve skills"),
            "domains": marvin.extract(question, instructions="Retrieve domains"),
            "keywords": marvin.extract(question, instructions="Retrieve keywords"),
            "entities": marvin.extract(question, instructions="Retrieve entities"),
        }
        # Append a dictionary containing the user input and its extraction results
        extraction_results.append({"question": question,"extractions": what_word_to_use})
    
    # Return the list of results
    return extraction_results

print(extraction_comparison(questions))

# @marvin.fn
# def ai_interpret_question(question: str) -> list:
#     """
#     Retrieve main technical concepts based on {{question}}
#     """
# print(ai_interpret_question("Can you help me build a REST API using Flask?"))
# print(ai_interpret_question(extraction_comparison("Can you help me build a REST API using Flask?"))
# for key, value in what_word_to_use.items():
#     print(f"{key.capitalize()}: {value}")
