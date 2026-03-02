arr=[10,2,34,55,3,99]
largest=first=second=0
for i in arr:
    if i > largest:
        second=largest
        largest=i
    elif i>second:
        second=i
print('SECOND:',second)