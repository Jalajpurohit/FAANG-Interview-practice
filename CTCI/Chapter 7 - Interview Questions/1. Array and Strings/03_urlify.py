'''
Problem Statement:
URLify - Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the 
additional characters and that you are given the "true" length of the string. (Note: If implementing in Java, please use a character array so that you can perform
this operation in place.

Example:
Input: "Mr Josh Smith", 13
Output: "Mr%20John%20Smith"

Hint 1: It's often easiest to modify strings by going from the end of the string to the beginning.
Hint 2: You might find you need to know the number of spaces. Can you just count them?
'''

# Solution 1: URLify without inbuilt python methods
# Time Complexity: O(N)
import unittest
def urlify_algo(string, length):
    """replace spaces with %20 and removes trailing spaces"""
    # convert to list because Python strings are immutable
    char_list = list(string)
    string = ""
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3 : new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return string.join(char_list)

# Solution 2: URLify with python replace() function
# Time Complexity: O(N)
def urlify_pythonic(text, length):
    """solution using standard library"""
    return text.rstrip().replace(" ", "%20")

# Solution 2: URLify with python replace() function
# Time Complexity: O(N)
def urlify_pythonic_v2(string, length):
    return '%20'.join(string.split())
  
# Unit tests
class Test(unittest.TestCase):
    """Test Cases"""

    test_cases = [
        ("much ado about nothing      ", "much%20ado%20about%20nothing"),
        ("Mr John Smith    ", "Mr%20John%20Smith"),
    ]
    testable_functions = [urlify_algo, urlify_pythonic, urlify_pythonic_v2]

    def test_urlify(self):
        for urlify in self.testable_functions:
            for test_string, expected in self.test_cases:
                stripped_length = len(test_string.rstrip(" "))
                actual = urlify(test_string, stripped_length)
                assert actual == expected


if __name__ == "__main__":
    unittest.main(exit=False)
