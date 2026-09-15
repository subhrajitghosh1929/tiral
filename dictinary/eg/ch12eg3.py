phoneDict={"madhav":1234567,"steven":7654321,"dilpreet":6734521,"Rabiya":4563217,"Murughan":3241567,"Sampree":4673215}
for a in phoneDict:
    print(a,":",phoneDict[a])
print(phoneDict.keys())
print(phoneDict.values())
if 7654321 in phoneDict.values():
    print("somebody has got that no.")
else:
    print("nobody has got that no.")
    
if 765432 in phoneDict.values():
    print("somebody has got that no.")
else:
    print("nobody has got that no.")

#2
print()
print("#2")
dict1={0:"value of key 0",1:"value for key 1","3":"value for a string -as-a-key",(4,5):"value for a tuple -as-a-key ","and for fun":7}
print(dict1[0])
print(dict1[(4,5)])
print(dict1[4,5])
print(dict1["3"])
dict1["3"]="change to new string"
print(dict1["3"])
dict1["new"]="new pair is added"
print(dict1["new"])

#3
print()
print("#3")
birdcount={"finch":10,"Myna":13,"Parakeet":16,"Hornbill":15,"Peacoke":15}
print(birdcount)
