n=153
temp=n
power=len(str(n))
sum=0
for i in range(n):
    digit=temp%10
    sum=sum+digit**power
    temp=temp//10
if sum==n:
    print("IT IS ARMSTRONG NUMBER:",sum)
else:
    print("it is not an armstrong number:",sum)
