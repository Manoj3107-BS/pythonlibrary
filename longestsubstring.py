class solution():
    def longestsubstring(self,s):
        char_wod=set()
        left=0
        max_count=0
        for right in range(len(s)):
            while s[right] in char_wod:
                char_wod.remove(s[left])
                left+=1
            char_wod.add(s[right])
            max_count=max(max_count,right-left+1)
        return max_count
s=('ababcbde')
sole=solution()
print(sole.longestsubstring(s))