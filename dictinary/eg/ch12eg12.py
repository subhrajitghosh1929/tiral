import json
s="This is a super ideal This \
idea will change the idea of learning"
word=s.split()
d={}
for one in word:
    key=one
    if key not in d:
        count=word.count(key)
        d[key]=count
print("conting frequencies in list \n",word)
print(json.dumps(d,indent=1))
