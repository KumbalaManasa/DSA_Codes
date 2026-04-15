def lar_el(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif target>arr[mid]:
            low = mid+1
        elif target<arr[mid]:
            high = mid-1
    return -1
arr = [1,5,6,3,2,4,9]
target = 3
print(lar_el(arr,target))           

    
            