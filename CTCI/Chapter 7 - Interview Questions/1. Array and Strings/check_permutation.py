# Problem Statement: Given two strings, write a method to decide if one is a permutation of the other.
# Hint 1: Describe what it means for two strings to be permutations of each other. Now, look at that definition you provided. Can you check the strings against that definition?
# Hint 2: There is one solution that is O(N log N) time. Another solution uses some space, but is O(N) time.
# Hint 3: Could a hash table be useful?
# Hint 4: Two strings that are permutations should have the same characters, but in different orders. Can you make orders the same?


# Solution 1: With use of list, a one pass solution
# Time Complexity: O(N)
NO_OF_CHARS = 256
def check_permutations_with_list(str1, str2):
	count = [0 for i in range(NO_OF_CHARS)]
	ind = 0
	n1 = len(str1)
	n2 = len(str2)
	if n1 != n2:
	    return False
	
	while ind < n1:
	    count[ord(str1[ind])] += 1
	    count[ord(str2[ind])] -= 1
	    ind += 1

	for i in range(NO_OF_CHARS):
		if count[i]:
		    return False;
	return True;

# Solution 2: With use of sorting
# Time Complexity: O(N**2) as QuickSort is being used in sorting. If use MergeSort than we can reduce time complexity to O(NlogN)
def check_permutations_with_sorting(s1, s2):
    l1 = len(str1)
    l2 = len(str2)
    
    if (n1 != n2):
        return False

    s1 = sorted(s1)
    s1 = " ".join(s1)
    s2 = sorted(s2)
    s2 = " ".join(s2)
 
    for i in range(0, n1, 1):
        if (str1[i] != str2[i]):
            return False
    return True
