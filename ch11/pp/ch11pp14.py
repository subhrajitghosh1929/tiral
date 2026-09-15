import statistics 
tup = eval(input("Enter a tuple: "))
tup_sum = sum(tup)
tup_len = len(tup)
print("Average of tuple element is:", tup_sum / tup_len)
print("Mean of tuple element is:", statistics.mean(tup))
