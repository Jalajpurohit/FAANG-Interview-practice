# Runtime Complexity: O(n)
# Space Complexity: O(1)

def pair_sum_sequence(n):
    sum = 0
    for i in range(n):
        sum += pair_sum(i, i+1)
    return sum

def pair_sum:
    return a + b
