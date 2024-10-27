import marvin
import pytest

# Simple Classification
def extract_sentiment(text:str):
    sentiment = marvin.classify(text,labels=["positive", "negative"])
    print(sentiment)
    return sentiment

# Simple Extraction
def extract_features(text:str):
    features = marvin.extract(text, instructions="product features")
    print(features)
    return features


# Extraction Test
def test_features():
    assert extract_features() == ["camera", "battery life"]


@pytest.mark.parametrize("text, expected", [
    ("Marvin is easy", "positive"),
    ("Marvin is terrible", "negative"),
    ]
    ) #test data
def test_sentiment(text, expected):

    result = extract_sentiment(text) # test code

    assert result == expected # assertion code

def ai_function(text):
    features = marvin.extract(text, instructions="product features")

    return features


class AI_Thing(BaseModel):
    text: str
    category: str

def test_features(text, expected_category):

    thing = AI_Thing(text, expected_category)

    assert thing.category == expected_category