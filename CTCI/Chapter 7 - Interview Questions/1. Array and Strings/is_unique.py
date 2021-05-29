# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hint 1: Try a Hash Table
# Hint 2: Could a bit vector be useful?
# Hint 3: Can you solve it in O(N logN) time? What might a solution like that look like?

# Solution 1: With Hash Table(basically dictionary in python)
# Run 1 loop with variable c and add it to dict after searching in char dictiornary. If found then False
# if entire for loop finishes then True
# Amortized Time Complexity: O(N) 
def is_unique_with_dict(s):
    char_dict = {}
    for c in s:
        if char_dict.get(c):
            return False
        else:
            char_dict[c] = 1
    return True
  
# Solution 2: Brute Force technique
# Run 2 loops with variable i and j. Compare str[i] and str[j]. If they become equal at any point, return false. 
# Time Complexity: O(N**2) 
def unique_characters_brute_force(str):
    for i in range(len(str)):
        for j in range(i + 1,len(str)):
            if(str[i] == str[j]):
                return False;
    return True;

# Solution 3 – Sorting: Using sorting based on ASCII values of characters 
# Time Complexity: O(N log N) 
def uniqueCharacters(st):
    sorted(st)
    for i in range(len(st)-1):
        # if at any time, 2 adjacent elements become equal, return false
        if (st[i] == st[i + 1]) :
            return False
    return True
  
# Solution 4 – Use of Extra Data Structure: This approach assumes ASCII char set(8 bits).
# The idea is to maintain a boolean array for the characters. The 256 indices represent 256 characters.
# All the array elements are initially set to false. As we iterate over the string, set true at the index equal to the int value of the character.
# If at any time, we encounter that the array value is already true, it means the character with that int value is repeated. 
# Time Complexity: O(n) using data structure
MAX_CHAR = 256;
def uniqueCharacters(str):
    # If length is greater than 256,
    # some characters must have been repeated
    if (len(str) > MAX_CHAR):
        return False;
    chars = [False] * MAX_CHAR;
    for i in range(len(str)):
        index = ord(str[i]);
 
        # If the value is already True, string has duplicate characters, return False
        if (chars[index] == True):
            return False;
        chars[index] = True;
 
    # No duplicates encountered, return True
    return True;
 
# Solution 5 – Without Extra Data Structure: The approach is valid for strings having alphabet as a-z. This approach is little tricky.
# Instead of maintaining a boolean array, we maintain an integer value called checker(32 bits).
# As we iterate over the string, we find the int value of the character with respect to ‘a’ with the statement int bitAtIndex = str.charAt(i)-‘a’; 
# Then the bit at that int value is set to 1 with the statement 1 << bitAtIndex . 
# Now, if this bit is already set in the checker, the bit AND operation would make checker > 0. Return false in this case. 
# Else Update checker to make the bit 1 at that index with the statement checker = checker | (1 <<bitAtIndex); 
# Time Complexity: O(n)  
# characters without using any data structure
import math 
def uniqueCharacters(str):
    # Assuming string can have characters a-z this has 32 bits set to 0
    checker = 0
    for i in range(len(str)):
        bitAtIndex = ord(str[i]) - ord('a')
 
        # If that bit is already set in
        # checker, return False
        if ((bitAtIndex) > 0):
            if ((checker & ((1 << bitAtIndex))) > 0):
                return False
                 
            # Otherwise update and continue by
            # setting that bit in the checker
            checker = checker | (1 << bitAtIndex)
 
    return True
 
# Solution 6: Using sets() in python:
# Time Complexity: O(nlogn)
# Convert the string to set. If the length of set is equal to length of string then return True else False.
def uniqueCharacters(str):
   
    # Converting string to set
    setstring = set(str)
     
    # If length of set is equal to len of string
    # then it will have unique characters
    if(len(setstring) == len(str)):
        return True
       
    return False
