import resources.ai
import pytest

def test_extract_subject() -> None:
    test_subject = resources.ai.extract_subject("How can I build an API?")
    assert test_subject == ['API']