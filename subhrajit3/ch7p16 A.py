import statistics
input_string = input('Enter elements separated by space \n')
user_list = input_string.split()
print('string list: ', user_list)
print()
# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])
print('User list: ', user_list)
# Calculating the sum of list elements
print("Sum = ", sum(user_list))
# Calculating the average of list elements
print("average = ", statistics.mean(user_list))
