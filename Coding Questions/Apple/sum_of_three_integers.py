# Runtime Complexity: Quadratic, O(n^2)
# Memory Complexity: Constant, O(1)O(1)
'''
Determine sum of three integers: The goal of this exercise is to determine if the sum of three integers is equal to the given value.
Problem statement: Given an array of integers and a value, determine if there are any three integers in the array whose sum equals the given value.
Solution: In this solution, we sort the array. Then, fix one element e and find a pair (a, b) in the remaining array so that required_sum - e is a + b.
Start with first element e in the array and try to find such a pair (a, b) in the remaining array (i.e A[i + 1] to A[n - 1]) that satisfies the condition: a+b = required_sum - e. If we find the pair, we have found the solution: a, b and e. Now we can stop the iteration.
Otherwise, we repeat the above steps for all elements e at index i = 1 to n - 3 until we find a pair that meets the condition.'''

def find_sum_of_two(A, val, start_index):
  i = start_index
  j = len(A) - 1
  while i < j:
    s = A[i] + A[j]
    if s == val:
      return True

    if s < val:
      i += 1
    else:
      j -= 1

  return False

def find_sum_of_three_v3(arr, required_sum):
  arr.sort()
  for i in range(0, len(arr)-2):
    remaining_sum = required_sum - arr[i]
    if find_sum_of_two(arr, remaining_sum, i+1):
      return True

  return False

arr = [-25, -10, -7, -3, 2, 4, 8, 10]

print(f'-8: {find_sum_of_three_v3(arr, -8)}')
print(f'-25: {find_sum_of_three_v3(arr, -25)}')
print(f'0: {find_sum_of_three_v3(arr, 0)}')
print(f'-42: {find_sum_of_three_v3(arr, -42)}')
print(f'-22: {find_sum_of_three_v3(arr, -22)}')
print(f'-7: {find_sum_of_three_v3(arr, -7)}')
print(f'-3: {find_sum_of_three_v3(arr, -3)}')
print(f'2: {find_sum_of_three_v3(arr, 2)}')
print(f'4: {find_sum_of_three_v3(arr, 4)}')
print(f'8: {find_sum_of_three_v3(arr, 8)}')
print(f'7: {find_sum_of_three_v3(arr, 7)}')
print(f'1: {find_sum_of_three_v3(arr, 1)}')
