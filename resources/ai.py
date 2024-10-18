# import marvin
# from resources.text import user_inputs

# def extraction_comparison(user_inputs):
#     # Initialize empty dictionary
#     extraction_results = []

#     # Loop through potential extraction words
#     for user_input in user_inputs:
#         what_word_to_use = {
#             "topics": marvin.extract(user_input, instructions="Retrieve topics"),
#             "technology": marvin.extract(user_input, instructions="Retrieve technologies"),
#             "concepts": marvin.extract(user_input, instructions="Retrieve concepts"),
#             "subjects": marvin.extract(user_input, instructions="Retrieve subjects"),
#             "skills": marvin.extract(user_input, instructions="Retrieve skills"),
#             "domains": marvin.extract(user_input, instructions="Retrieve domains"),
#             "keywords": marvin.extract(user_input, instructions="Retrieve keywords"),
#             "entities": marvin.extract(user_input, instructions="Retrieve entities"),
#         }
#         # Append a dictionary containing the user input and its extraction results
#         extraction_results.append({"user_input": user_input,"extractions": what_word_to_use})
    
#     # Return the list of results
#     return extraction_results

# for key, value in what_word_to_use.items():
#     print(f"{key.capitalize()}: {value}")


# @marvin.fn
# def ai_interpret_user_input(user_input: str) -> list:
#     """
#     Retrieve main technical concepts based on {{user_input}}
#     """
# print(ai_interpret_user_input(user_input))

# @marvin.fn
# def ai_response(user_input: str, concepts: str) -> str:
#     """
#     Respond in naturally language to confirm concepts on interest. Suggest relevant python frameworks related to the concepts.
#     """

# print(ai_response(user_input, concepts))

# @marvin.fn
# def list_tech(name:str) -> list[str]: """pick and appropriate framework for each topic."""

# tech = list_tech(concepts)

# print(tech)

# one_tech = marvin.extract(tech, instructions="only 1 product")

# print(one_tech)
