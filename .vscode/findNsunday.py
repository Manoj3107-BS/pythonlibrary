start="mon"
N=13
days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
index=days.index(start)
count=0
for i in range(N):
    current_day=days[(index+i)%7]
    if current_day=="sun":
        count+=1
print('NUMBER OF SUNDAY:',count)