import marvin
marvin.settings.openai.api_key = 'sk-proj-qyw18WnAby266IKbQvIIT3BlbkFJXb1kEvR4467lNK4sFKh7'

result = marvin.classify(
    "Marvin is so easy to use!",
    labels=["positive", "negative"],
)
print(result)


features = marvin.extract(
    "I love my new phone's camera, but the battery life could be improved.",
    instructions="product features",
)

print(features)