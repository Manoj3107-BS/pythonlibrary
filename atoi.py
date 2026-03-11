class solution():
    def myatoi(self,s):
        n=len(s)
        num=0
        i=0
        sign=1
        while i<n and s[i]==' ':
            i+=1
        if i<n and (s[i]=='+' or s[i]=='-'):
            if s[i]=='-':
                sign=-1
            i+=1
        while i<n and s[i].isdigit():
            dig=int(s[i])
            num=num*10+dig
            i+=1
        num=num*sign
        if num<-2**31:
            return 2**31
        if num>2**31-1:
            return 2**31-1
        return num
obj=solution()
s=' 3456ad'
print(obj.myatoi(s))