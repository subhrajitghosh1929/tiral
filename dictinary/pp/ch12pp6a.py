# Modified ch12 Q-6 pg- sa 448
days_in_months = {
    "january":31,
    "february":28,
    "march":31,
    "april":30,
    "may":31,
    "june":30,
    "july":31,
    "august":31,
    "september":30,
    "october":31,
    "november":30,
    "december":31
}
m = input("Enter name of month: ")
if m not in days_in_months:
    print("Please enter the correct month")
else:
    print("a) There are", days_in_months[m], "days in", m)

print("b) Months in alphabetical order are:", sorted(days_in_months))
print()

print("c) Months with 31 days:", end=" ")
for i in days_in_months:
    if days_in_months[i] == 31:
        print(i, end=" ")
print("-------------------------------------------------------------")         
print()        
day_month_lst = []
for i in days_in_months:    # converting dict to list
    day_month_lst.append([days_in_months[i], i])  # order of dict changed in list to value:key  
print(day_month_lst)
day_month_lst.sort()    # dict cannot be sorted 
print("--->",day_month_lst)

print()
month_day_lst =[]
for i in day_month_lst:
    month_day_lst.append([i[1], i[0]])   # order of list value:key  changed in list to key:value
sorted_days_in_months = dict(month_day_lst)     # LIST converted to dict  
print("d) Months sorted by days:", sorted_days_in_months)
