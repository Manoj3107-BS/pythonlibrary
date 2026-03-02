a='asdndbeh1234fbU'
v='aeiouAEIOU'
vowels=0
con=0
dig=0
for i in a:
    if i in v:
        vowels+=1
    if i.isalpha():
        con+=1
    if i.isdigit():
        dig+=1
print('vowels:',vowels)
print('con:',con)
print('dig:',dig)