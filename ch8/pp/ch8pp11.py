sum = count = 0

print("Enter numbers")
print("(Enter 'q' to see the average)")

while True :
    n = input()
    if n == 'q' or n == 'Q' :
        break
    else :
        sum += int(n)
        count += 1

avg = sum / count
print("Average = ", avg)
