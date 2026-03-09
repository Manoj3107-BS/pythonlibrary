class solution():
    def medianoftwo(self,num1,num2):
        num=num1+num2
        num.sort()
        n=len(num)
        if n%2==0:
            return (num[n//2-1]+num[n//2]/2)
        else:
            return num[n//2]
num1=[1,3]
num2=[2]
sol=solution()
print(sol.medianoftwo(num1,num2))