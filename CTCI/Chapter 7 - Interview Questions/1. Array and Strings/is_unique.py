# Problem Statment: Is Unique - Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hint 1: Try a Hash Table
# Hint 2: Could a bit vector be useful?
# Hint 3: Can you solve it in O(N logN) time? What might a solution like that look like?

import time
import unittest
from collections import defaultdict

# Solution 1: Brute Force technique
# Time Complexity: O(N**2) 
def is_unique_chars_brute_force(string: str) -> bool:
    for i in range(len(string)):
        for j in range(i + 1,len(string)):
            if(string[i] == string[j]):
                return False;
    return True;


# Solution 2 – Use of Extra Data Structure: This approach assumes ASCII char set(8 bits).
# Time Complexity: O(N)
def is_unique_chars_algorithmic(string: str) -> bool:
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True
    return True



# Solution 3: Using sets() in python:
# Time Complexity: O(N logN)
def is_unique_chars_pythonic(string: str) -> bool:
    return len(set(string)) == len(string)


# Solution 4 – Without Extra Data Structure
# Time Complexity: O(N)  
def is_unique_bit_vector(string: str) -> bool:
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True


# Solution 5: With Hash Table(basically dictionary in python)
# Time Complexity: O(N) Amortized
def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if character_counts.get(char:
            return False
        character_counts[char] = 1
    return True

                                
# Solution 6 – Using sorting
# Time Complexity: O(N log N) 
def is_unique_chars_sorting(string: str) -> bool:
    sorted_string = sorted(string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
    ]
    test_functions = [
        is_unique_chars_brute_force,
        is_unique_chars_pythonic,
        is_unique_chars_algorithmic,
        is_unique_bit_vector,
        is_unique_chars_using_dictionary,
        is_unique_chars_sorting,
    ]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main(exit=False)
