a=[1,0,6,4,0,6,7,0]
j=0
for i in range(len(a)):
    if a[i]!=0:
        a[j]=a[i]
        j+=1
while j<len(a):
    a[j]=0
    j+=1
print(a)