def rem_dup(arr):
    index = 0
    seen = set()

    for num in arr:
        if num not in seen:
            seen.add(num)
            arr[index]=num
            index+=1
           
    return index
arr = [1,2,2,2,3,4,5,6]
k= rem_dup(arr)
print("k=",rem_dup(arr))
print("arr after removing duplicates", arr[:k])        