first=0
second=1
print(first)
print(second)
for a in range(1,19):
    third=first+second
    print(a+2,"   ",third)
    first,second=second,third
