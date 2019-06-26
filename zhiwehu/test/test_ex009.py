from src.ex009 import *
import pytest

def test_capitalize_lines():
    lines = ['Hello world', 'Practice makes perfect']
    capitalized_lines = capitalize_lines(lines)

    assert capitalized_lines == ['HELLO WORLD', 'PRACTICE MAKES PERFECT']