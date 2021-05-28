# Runtime Complexity: O(N**2)

def print_pair(arr):
    for i in arr:
        for j in arr:
            print(i,j)

print_pair([1,2,3])

'''
Result:
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3
'''
