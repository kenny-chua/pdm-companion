import marvin

# Simple Classification
def extract_sentiment():
    sentiment = marvin.classify("Marvin is so easy to use!",labels=["positive", "negative"])
    print(sentiment)
    return sentiment

# Simple Extraction
def extract_features():
    features = marvin.extract("I love my new phone's camera, but the battery life could be improved.", instructions="product features")
    print(features)
    return features

# Classification Test
def test_sentiment():
    assert extract_sentiment() == "positive"

# Extraction Test
def test_features():
    assert extract_features() == ["camera", "battery life"]
