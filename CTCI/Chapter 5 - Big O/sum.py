# Runtime Complexity: O(n)
# Space Complexity: O(n)

def sum(n):
    if n<=0:
      return 0
    return n + sum(n-1)
