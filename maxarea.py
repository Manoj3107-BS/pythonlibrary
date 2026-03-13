class solution():
    def maxarea(self,H):
        left=0
        right=len(H)-1
        max_count=0
        while left<right:
            dept=right-left
            area=min(H[left],H[right])*dept
            max_count=max(max_count,area)
            if H[left]<H[right]:
                left+=1
            else:
                right-=1
        return max_count
sol=solution()
H=[1,2,3,6,7,9,5,6]
print(sol.maxarea(H))