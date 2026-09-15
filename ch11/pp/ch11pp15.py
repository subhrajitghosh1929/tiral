tup1 = ((1, 2), (3, 4.15, 5.15), ( 7, 8, 12, 15))
total_mean = 0
tup1_len = len(tup1)
for i in range(tup1_len):
    mean = sum(tup1[i]) / len(tup1[i])
    print("Mean element", i + 1, ":", mean)
    total_mean = total_mean + mean
print("Mean of means" ,total_mean / tup1_len)
