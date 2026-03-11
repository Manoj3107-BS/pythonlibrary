class solution():
    def palindrome(self,s):
        s=str(s)
        if s==s[::-1]:
            return True
        else:
            return False
s=-121
sol=solution()
print(sol.palindrome(s))
