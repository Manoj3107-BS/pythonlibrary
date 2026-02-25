def count_greater(arr):
    if not arr:
        return 0
    max_val=arr[0]
    count=1
    for i in range(1,len(arr)):
        if arr[i]>max_val:
            max_val=arr[i]
            count+=1
    return count
arr=[3,4,1,9,11,8,15]
result=count_greater(arr)
print(result)