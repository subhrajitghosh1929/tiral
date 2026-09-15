hr = int(input("Enter hour between 1-12 : "))
n = int(input("How many hours ahead : "))

s = hr + n

if s > 12:
    s -= 12

print("Time at that time would be : ", s, "O'clock")
