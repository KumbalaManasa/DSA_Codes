def largest(arr):
    lar = arr[0]
    for i in range(1,len(arr)):
        if arr[i]>lar:
            lar = arr[i]
    return lar
arr = [3,2,1,5,6]
print(largest(arr))

#Time Complexity: O(N), where N is the size of the array, as we are iterating through the array once.
#Space Complexity: O(1), as we are using a constant 