n=10
binary=bin(n)[2:]
print(binary)
toggled=''
for bit in binary:
    if bit==0:
        toggled+='1'
    else bit==1:
        toggled+='0'
print(toggled)
result=int(toggled,2)
print(result)