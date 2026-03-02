a='banana'
count={}
for i in a:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
max_ch=max(count,key=count.get)
print('max_char:',max_ch)
print('count:',count[max_ch])
