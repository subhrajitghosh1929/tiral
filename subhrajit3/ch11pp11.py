seq_a = eval(input("Enter the first tuple: "))
seq_b = eval(input("Enter the second tuple: "))
for i in seq_a:
    if i not in seq_b:
        print("False")
        break
else:
    print("True")
