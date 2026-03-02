import pytest

#Import the function that implements actual tests
from lib.palindrome import longest_palindromic_substring

#Implement the test function
def test_longest_palindromic_substring():

    # use logical OR to evaluate two expected ouputs of the same inputs
    assert longest_palindromic_substring("babad") == "bab" or longest_palindromic_substring("babad") == "aba"
    assert longest_palindromic_substring("cbbd") == "bb"
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("ac") == "a" or longest_palindromic_substring("ac") == "c"
    assert longest_palindromic_substring("racecar") == "racecar"