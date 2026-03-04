num=29
if num<=1:
    print("IT IS NOT PRIME NUMBER")
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print("IT IS NOT PRIME NUMBER")
        break
else:
    print("IT IS PRIME NUMBER")