# Runtime Complexity: O(N)

def foo(arr):
    sum_val = 0
    product = 1
    
    for i in arr:
        sum_val += i
    
    for j in arr:
        product *= j
        
    print(sum_val, product)

foo([1,2,3,4,5]) # 15,120
