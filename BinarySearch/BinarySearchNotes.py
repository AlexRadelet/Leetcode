A = [-3, -1, 0 , 1, 4,7]

#Naive O(n) search
if -1 in A:
    print(True)

# Traditional Binary Search - Looking up if number is in array :
# Time : O(log n)
# Space : O(1)
def binary_search(arr, target):
    N = len(A)
    L = 0
    R = N-1

    # <= because we need to check the final value
    while L <= R:
        #Optimal way to calcul M
        M = L + ((R-L)//2)
        if arr[M] == target:
            return True
        elif  target < arr[M]:
            R = M-1
        else:
            L = M+1
    return False

print(binary_search(A, -1))

# Based on a condition
# [ F, F, F, T, T]
B = [False, False, False, False, False, False, True]

def binary_search_condition(arr):
  N = len(arr)
  L = 0
  R = N - 1

  #We need to find the index where L = R
  while L < R:
    M = (L + R) // 2

    #Condition based on the problem
    if B[M]:
      R = M
    else:
      L = M + 1
    #We can return R, they are the same index
  return L

print(binary_search_condition(B))
