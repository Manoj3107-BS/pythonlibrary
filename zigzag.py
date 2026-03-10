class solution():
    def convert(self,s,numrows):
        if numrows==1 or numrows>len(s):
            return s
        row=['']*numrows
        current_rows=0
        direction=-1
        for char in s:
            row[current_rows]+=char
            if current_rows==0 or current_rows==numrows-1:
                direction=-direction
            current_rows+=direction
        return ''.join(row)
s="PAYPALISHIRING"
numrows=3
sol=solution()
print(sol.convert(s,numrows))