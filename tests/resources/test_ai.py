from src.pdm_companion.resources import ai as ai
import pytest  # only needed to use fixtures
from config import _openaisecret  # type: ignore  # noqa: F401


# If the result type is a list
def test_list_extract_subject():
    test_subject = ai.extract_subject("How can I build an API?")
    assert isinstance(test_subject, list)


# Basic Test
def test_extract_subject() -> None:
    test_subject = ai.extract_subject("How can I build an API?")
    assert test_subject == ["API"]


# --------------------------------------
# Using Fixture then test
@pytest.fixture
def question_fixture():
    return "How can I convert ISO time to human-readable time?"


def test_with_fixture_extract_subject(question_fixture):
    assert ai.extract_subject(question_fixture) == ["ISO Time"]


# --------------------------------------
# Parametrization (Spelling is wrong HAHA)


@pytest.mark.parametrize(
    "name_of_fixture, expected_test_results",
    [
        ("How can I build an API?", ["API"]),
        ("How can I verify a data structure?", ["Data Structure"]),
        ("How can I convert ISO time to human-readable time?", ["ISO Time"]),
        ("How do I scrape a webpage?", ["Scrape a Webpage"]),
        ("What should I use to handle SQL databases in Python?", ["SQL Databases in Python"]),
        ("How can I create a GUI for my Python application?", ["GUI for Python Application"]),
        ("How can I parallelize tasks in Python?", ["parallelize tasks in Python"]),
        ("How can I test my Python code?", ["Testing Python Code"]),
        ("What can I use to handle HTTP requests?", ["Http Requests"]),
        ("How do I work with machine learning in Python?", ["machine learning"]),
    ],
)
def test_with_paratrization_fixture(name_of_fixture, expected_test_results):
    # Since AI answers are unpredictable, I want to make both results from Marvin and expected results to all lowercase.
    results_directly_from_marvin = ai.extract_subject(name_of_fixture)

    # Convert both expected and actual results to lowercase for comparison
    expected_test_results_lower = [item.lower() for item in expected_test_results]
    marvin_results_lower = [item.lower() for item in results_directly_from_marvin]

    assert marvin_results_lower == expected_test_results_lower
