#The upper bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than the given key i.e. x.
#Optimal approach: TC = O(logN) SC = O(1)
def upper_b(arr,key):
    n = len(arr)
    low = 0
    high = n-1
    ans = len(arr)
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>key:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans
arr = [3, 5, 8, 9, 15, 19]
x = 9
print(upper_b(arr,x))        

'''#brute force TC = O(N) SC = O(1)
def upper_b(arr,key):
    for i in range(len(arr)):
        if arr[i]>key:
            return i
    return -1
arr = [3, 5, 8, 9, 15, 19]    
x = 9
print(upper_b(arr,x))'''

