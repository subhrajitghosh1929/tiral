while True :
    str = input("Please enter a sentence, or 'q' to quit : ")
    newStr = ""
    if str.lower() == "q" :
        break
    for ch in str :
        if ch.islower() :
            newStr += ch.upper()
        elif ch.isupper() :
            newStr += ch.lower()
        else :
            newStr += ch
    print(newStr)
