import random
import statistics
seq=[]
for i in range(6):
    a = int(random.randrange(10,30))
    seq.append(a)
    print(seq)

mean = statistics.mean(seq)
median = statistics.median(seq)
mode = statistics.mode(seq)
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print(type(seq))


