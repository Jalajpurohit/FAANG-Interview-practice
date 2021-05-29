# Problem Statement: Check Permutations - Given two strings, write a method to decide if one is a permutation of the other.
# Hint 1: Describe what it means for two strings to be permutations of each other. Now, look at that definition you provided. Can you check the strings against that definition?
# Hint 2: There is one solution that is O(N log N) time. Another solution uses some space, but is O(N) time.
# Hint 3: Could a hash table be useful?
# Hint 4: Two strings that are permutations should have the same characters, but in different orders. Can you make orders the same?

import unittest
from collections import Counter

# Solution 1: With use of list
# Time Complexity: O(N)
def check_permutation_by_count(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = [0] * 256
    for c in str1:
        counter[ord(c)] += 1
    for c in str2:
        if counter[ord(c)] == 0:
            return False
        counter[ord(c)] -= 1
    return True


# Solution 2: With use of sorting
# Time Complexity: O(N**2) as QuickSort is being used in sorting. If use MergeSort than we can reduce time complexity to O(NlogN)
def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True


# Solution 3: Pythonic Solution
def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False

    return Counter(str1) == Counter(str2)


class Test(unittest.TestCase):
    # str1, str2, is_permutation
    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    testable_functions = [
        check_permutation_by_sort,
        check_permutation_by_count,
        check_permutation_pythonic,
    ]

    def test_cp(self):
        # true check
        for check_permutation in self.testable_functions:
            for str1, str2, expected in self.test_cases:
                assert check_permutation(str1, str2) == expected


if __name__ == "__main__":
    unittest.main(exit=False)
