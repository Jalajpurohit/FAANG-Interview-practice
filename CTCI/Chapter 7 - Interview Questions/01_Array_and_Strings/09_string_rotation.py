'''
Problem Statement:
String Rotation - Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2,
write code to check if s2 is a rotation of s1 using only one call to isSubstring

Example:
'waterbottle' is a rotation of 'erbottlewat'

Hint 1: If a string is a rotation of another, then it's a rotation at a particular point.
For example, a rotation of waterbottle at character 3 means cutting waterbottle at character 3 and putting the right half erbottle before the left haf wat.
Hint 2: We are essentially asking if there's a way of splitting the first string into two parts, x and y, such that the first string xy and second string is yx.
For example, x = wat and y = erbottle. The first string is xy = waterbottle. The second string is yx = erbottlewat.
Hint 3: Think about the earlier hint. Then think about what happens when you concatenate erbottleawt to itself. You get erbottlewaterbottlewat.
'''

import unittest

# worst solution
def is_substring(s1,s2):
    for i in range(len(s1)):
        if s1[i+1:]+s1[:i+1] == s2:
            return True
    return False

# best solution
# Time complexity: O(N)
def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return s2 in s1 * 2
    return False


class Test(unittest.TestCase):

    test_cases = [
        ("waterbottle", "erbottlewat", True),
        ("foo", "bar", False),
        ("foo", "foofoo", False),
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.test_cases:
            actual = string_rotation(s1, s2)
            assert actual == expected
            actual = is_substring(s1,s2)
            assert actual == expected


if __name__ == "__main__":
    unittest.main(exit=False)
