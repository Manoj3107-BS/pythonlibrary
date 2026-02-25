def odd_num(arr):
    result=0
    for i in arr:
        result^=i
    return result
b=odd_num([2,3,4,4,2])
print(b)