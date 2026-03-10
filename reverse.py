class solution():
    def reverse(self,x):
        if x<0:
            sign=-1
            x=-x
        else:
            sign=1
        rev=0
        while x!=0:
            dig=x%10
            rev=rev*10+dig
            x=x//10
        rev*=sign
        return rev
sol=solution()
print(sol.reverse(123))
print(sol.reverse(-567))
